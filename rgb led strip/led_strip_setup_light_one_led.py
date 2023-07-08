import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip Pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Select the first LED and set the colour to red
strip[0] = (255,0,0)

# Send the data to the strip
strip.write()