import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip Pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Fill the entire strip with same colour
strip.fill((72,209,204))

# Send the data to the strip
strip.write()