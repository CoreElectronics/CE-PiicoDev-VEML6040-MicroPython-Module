# PiicoDev® Colour Sensor VEML6040 MicroPython Module

This is the firmware repo for the [Core Electronics PiicoDev® Colour Sensor VEML6040](https://core-electronics.com.au/catalog/product/view/sku/CE07823)

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified), include `PiicoDev_Unified.py` in the project directory on your MicroPython device.

<!-- TODO update tutorial link with the device tinyurl eg. piico.dev/p1
See the [Quickstart Guide](https://piico.dev/pX)
 -->

# Usage
## Example
[main.py](https://github.com/CoreElectronics/CE-PiicoDev-VEML6040-MicroPython-Module/blob/main/main.py) is a simple example to get started.
```
# PiicoDev VEML6040 minimal example code
# This program reads light data from the PiicoDev VEML6040 Colour Sensor
# Displays Raw Data, and classifies colours as fruits

from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms

fruitList = {
   "apple":0,
   "carrot":60,
   "lime":120
   }

colourSensor = PiicoDev_VEML6040()

while True:
    ### Example 1: Print Raw RGB Data
    data = colourSensor.readRGB() # Read the sensor (Colour space: Red Green Blue)
    red = data['red'] # extract the RGB information from data
    grn = data['green']
    blu = data['blue']

    print(str(blu) + " Blue  " + str(grn) + " Green  " + str(red) + " Red") # Print the data. Printing as BGR so the Thonny plot-colours match nicely :)

    ### Example 2: Classify the colour being shown - eg. a fruit sorting machine
#   data = colourSensor.readHSV() # Read the sensor (Colour space: Hue Saturation Value)
#   hue = data['hue'] # extract the Hue information from data

#   label = colourSensor.classifyHue() # Read the sensor again, this time classify the colour
#   print(str(label) + " Hue: " + str(hue)) # Show the label and the corresponding hue
    sleep_ms(1000)
```
## Details
### `PiicoDev_VEML6040(bus=, freq=, sda=, scl=, addr=0x10)`
Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
bus | int | 0,1 | Raspberry Pi Pico: 0, Raspberry Pi: 1 | I2C Bus.  Ignored on Micro:bit
freq | int | 100-1000000 | Device dependent | I2C Bus frequency (Hz).  Ignored on Raspberry Pi
sda | Pin | Device Dependent | Device Dependent | I2C SDA Pin. Implemented on Raspberry Pi Pico only
scl | Pin | Device Dependent | Device Dependent | I2C SCL Pin. Implemented on Raspberry Pi Pico only
addr | int | 0x10 | 0x10 | This address cannot be changed

### `PiicoDev_VEML6040.readRGB()`
Returns a dictionary with the Red, Green & Blue colour space.

Parameter | Type | Unit | Description
--- | --- | --- | ---
red | float |  | Red reading
green | float | | Green reading
blue | float | | Blue reading
white | float | Lux | Ambient light
cct | float | K | Colour temperature

### `PiicoDev_VEML6040.readHSV()`
Returns a dictionary with the Hue Saturation Value colour space.

Parameter | Type | Unit | Description
--- | --- | --- | ---
hue | float |  | Hue reading
sat | float | | Saturation reading
val | float | | Value reading

### `PiicoDev_VEML6040.classifyHue(hues={"red":0,"yellow":60,"green":120,"cyan":180,"blue":240,"magenta":300}, min_brightness=0)`
Returns a classification of the hue.

Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
red | float | 0 - 360 | 0 | Red hue value
yellow | float | 0 - 360 | 60| Yellow hue value
green | float | 0 - 360 | 120 | Green hue value
cyan | float | 0 - 360 | 180| Cyan hue value
blue | float | 0 - 360 | 240| Blue hue value
magenta | float | 0 - 360 | 300 | Magenta hue value
min_brightness | float | 0 - 1 | 0 | The brightness of the measurement must be above this level to assign a colour classification.  If the measured brightness is below the min_brightness threshold, the returned classification is `None`

# License
This project is open source - please review the LICENSE.md file for further licensing information.

If you have any technical questions, or concerns about licensing, please contact technical support on the [Core Electronics forums](https://forum.core-electronics.com.au/).

*\"PiicoDev\" and the PiicoDev logo are trademarks of Core Electronics Pty Ltd.*
