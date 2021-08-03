# A simple class to read data from the VEML6040 i2c light sensor
# Outputs:
#  - raw values for Red, Green, Blue and White
#  - Ambient light, based on the green value
#  - Correlated colour temperature (CCT)

# This module has been tested with the following development boards:
#    • BBC Micro:bit
#    • Raspberry Pi Pico (RP2040)

# No warranties express or implied, including any warranty of merchantability and warranty of fitness for a particular purpose.
# Written by Peter Johnston at Core Electronics May 2021

from PiicoDev_Unified import *
i2c = PiicoDev_Unified_I2C()
from utime import sleep_ms

# Registers
_veml6040Address = 0x10
_CONF = b'\x00'
_REG_RED = b'\x08'
_REG_GREEN = b'\x09'
_REG_BLUE = b'\x0A'
_REG_WHITE = b'\x0B'

_DEFAULT_SETTINGS = b'\x00' # initialise gain:1x, integration 40ms, Green Sensitivity 0.25168, Max. Detectable Lux 16496
                            # No Trig, Auto mode, enabled.
_SHUTDOWN = b'\x01'         # Disable colour sensor
_INTEGRATION_TIME = 40      # ms
_G_SENSITIVITY = 0.25168    # lux/step
    
class PiicoDev_VEML6040(object):    
    def __init__(self, addr=_veml6040Address, i2c_=i2c):
        self.i2c = i2c_
        self.addr = addr
        try:
            self.i2c.write8(self.addr, _CONF, _SHUTDOWN)
            self.i2c.write8(self.addr, _CONF, _DEFAULT_SETTINGS) 
        except Exception:
            print('Device 0x{:02X} not found'.format(self.addr))
            
    # Read colours from VEML6040
    # Returns raw red, green and blue readings, ambient light [Lux] and colour temperature [K]
    def read(self):
        raw_data = self.i2c.read16(self.addr, _REG_RED)        # returns a bytes object   
        data_red_int = int.from_bytes(raw_data, 'little')
        
        raw_data = (self.i2c.read16(self.addr, _REG_GREEN))    # returns a bytes object
        data_green_int = int.from_bytes(raw_data, 'little')
        
        raw_data = (self.i2c.read16(self.addr, _REG_BLUE))     # returns a bytes object
        data_blue_int = int.from_bytes(raw_data, 'little')
        
        raw_data = (self.i2c.read16(self.addr, _REG_WHITE))    # returns a bytes object
        data_white_int = int.from_bytes(raw_data, 'little')
        
        # Generate the XYZ matrix based on https://www.vishay.com/docs/84331/designingveml6040.pdf
        colour_X = (-0.023249 * data_red_int) + (0.291014 * data_green_int) + (-0.364880 * data_blue_int)
        colour_Y = (-0.042799 * data_red_int) + (0.272148 * data_green_int) + (-0.279591 * data_blue_int)
        colour_Z = (-0.155901 * data_red_int) + (0.251534 * data_green_int) + (-0.076240 * data_blue_int)
        colour_x = colour_X / (colour_X + colour_Y + colour_Z)
        colour_y = colour_Y / (colour_X + colour_Y + colour_Z)
        
        # Use McCamy formula
        colour_n = (colour_x - 0.3320)/(0.1858 - colour_y)
        colour_CCT = 449.0 * colour_n ** 3 + 3525.0 * colour_n ** 2 + 6823.3 * colour_n + 5520.33
        
        # Calculate ambient light in Lux
        colour_ALS = data_green_int * _G_SENSITIVITY
        
        return data_red_int, data_green_int, data_blue_int, data_white_int, colour_ALS, colour_CCT

