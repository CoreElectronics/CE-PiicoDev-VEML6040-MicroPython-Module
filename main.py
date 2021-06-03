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
    red = lightVal[0]
    grn = lightVal[1]
    blu = lightVal[2]
#     print(str(blu) + " Blue  " + str(grn) + " Green  " + str(red) + " Red")

# Uncomment the code below to expose additional functionality
    total_colours = red + grn +  blu
          
#     # Extract each colour's contribution
    red_c = red/total_colours
    green_c = grn/total_colours
    blue_c = blu/total_colours
  
#     # Categorise the colour being read with a description.  This is a simple demo that has not 
    colour_description = "uncategorised"
    if ((red_c > 0.4) and (green_c <= 0.4) and (blue_c <= 0.3)): 
        colour_description = "red"
    if ((red_c <= 0.4) and (green_c > 0.4) and (blue_c <= 0.2)):
        colour_description = "green"
    if ((red_c <= 0.35) and (green_c <= 0.45) and (blue_c > 0.25)):
        colour_description = "blue"
    if ((red_c > 0.35) and (red_c <= 0.42) and (green_c > 0.40) and (green_c <= 0.45) and (blue_c < 0.2)):
        colour_description = "yellow"
    print("{} B  {:5.0f} G  {:5.0f} R makes {}".format(blu, grn, red, colour_description))
    
    sleep(0.1)
    
    
#     print("{} R  {:5.0f} G  {:5.0f} B  {:5.0f} W  {:5.3f} Lux  {:5.0f} K {} ".format(red, grn, blu, lightVal[3], lightVal[4], lightVal[5], colour_description))