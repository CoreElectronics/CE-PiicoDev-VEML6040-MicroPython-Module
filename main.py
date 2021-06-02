# PiicoDev VEML6030 minimal example code
# This program reads light data from the PiicoDev VEML6040 ambient light sensor
# and displays the result

import sys
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from time import sleep

colourSensor = PiicoDev_VEML6040()

sleep(1)

while True:
    lightVal = colourSensor.read()
    total_colours = lightVal[0] + lightVal[1] +  lightVal[2]
    
    # Extract each colour's contribution
    red_c = lightVal[0]/total_colours
    green_c = lightVal[1]/total_colours
    blue_c = lightVal[2]/total_colours
    
    # Categorise the colour being read with a description.  This is a simple demo that has not 
    colour_description = "uncategorised"
    if ((red_c > 0.4) and (green_c <= 0.4) and (blue_c <= 0.2)): 
        colour_description = "red"
    if ((red_c <= 0.4) and (green_c > 0.43) and (blue_c <= 0.2)):
        colour_description = "green"
    if ((red_c <= 0.35) and (green_c <= 0.45) and (blue_c > 0.25)):
        colour_description = "blue"
    if ((red_c > 0.35) and (red_c <= 0.42) and (green_c > 0.40) and (green_c <= 0.45) and (blue_c < 0.2)):
        colour_description = "yellow"
    print("{} R  {} G  {} B  {} W  {} Lux  {} K {} ".format(lightVal[0], lightVal[1], lightVal[2], lightVal[3], lightVal[4], lightVal[5], colour_description))
    
    sleep(1)
    
