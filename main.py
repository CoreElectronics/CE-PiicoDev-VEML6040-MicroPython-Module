# PiicoDev VEML6030 minimal example code
# This program reads light data from the PiicoDev VEML6030 ambient light sensor
# and displays the result

from PiicoDev_VEML6040 import PiicoDev_VEML6040
from utime import sleep_ms

# Initialise Sensor
light = PiicoDev_VEML6040()

while True:
    # Read and print light data
    lightVal = light.read()
    print("{} R  {} G  {} B  {} W  {} Lux  {} K".format(lightVal[0], lightVal[1], lightVal[2], lightVal[3], lightVal[4], lightVal[5]))
    
    sleep_ms(1000)