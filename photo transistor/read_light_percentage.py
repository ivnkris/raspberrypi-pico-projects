#Imports
from machine import ADC, Pin
from time import sleep

# Define ADC Pin for light sensor
lightsensor = ADC(Pin(26))

# Read analouge sensor value
light = lightsensor.read_u16()

# Turn reading into percentage
lightpercent = round(light / 65535 * 100, 2)

print(lightpercent)