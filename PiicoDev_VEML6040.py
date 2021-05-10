# A simple class to read data from the VEML6040 i2c light sensor

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
            self.i2c.UnifiedWrite(self.addr, _CONF + _SHUTDOWN)
            self.i2c.UnifiedWrite(self.addr, _CONF + _DEFAULT_SETTINGS) 
        except Exception:
            print('Device 0x{:02X} not found'.format(self.addr))
            
        
    def read(self):
        self.i2c.UnifiedWrite(self.addr, _REG_RED, stop=False)  # write address and repeat condition
        sleep_ms(_INTEGRATION_TIME)
        raw_data = (self.i2c.UnifiedRead(self.addr, 2))         # returns a bytes object     
        data_red_int = int.from_bytes(raw_data, 'little') * _G_SENSITIVITY
        
        self.i2c.UnifiedWrite(self.addr, _REG_GREEN, stop=False)# write address and repeat condition
        sleep_ms(_INTEGRATION_TIME)
        raw_data = (self.i2c.UnifiedRead(self.addr, 2))         # returns a bytes object
        data_green_int = int.from_bytes(raw_data, 'little') * _G_SENSITIVITY
        
        self.i2c.UnifiedWrite(self.addr, _REG_BLUE, stop=False) # write address and repeat condition
        sleep_ms(_INTEGRATION_TIME)
        raw_data = (self.i2c.UnifiedRead(self.addr, 2))         # returns a bytes object
        data_blue_int = int.from_bytes(raw_data, 'little') * _G_SENSITIVITY
        
        self.i2c.UnifiedWrite(self.addr, _REG_WHITE, stop=True) # write address and repeat condition
        sleep_ms(_INTEGRATION_TIME)
        raw_data = (self.i2c.UnifiedRead(self.addr, 2))         # returns a bytes object
        data_white_int = int.from_bytes(raw_data, 'little') * _G_SENSITIVITY
        
        return data_red_int, data_green_int, data_blue_int, data_white_int
          
