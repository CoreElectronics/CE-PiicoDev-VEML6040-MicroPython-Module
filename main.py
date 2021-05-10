# PiicoDev VEML6040 minimal example code
# This program reads light data from the PiicoDev VEML6040 ambient light sensor
# and displays the result

from PiicoDev_VEML6040 import PiicoDev_VEML6040
from utime import sleep_ms

# Initialise Sensor
light = PiicoDev_VEML6040()

while True:
    # Read and print light data
    lightVal = light.read()
    print("{} lux".format(lightVal))
    
    sleep_ms(1000)