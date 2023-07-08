import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip Pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Colour variables
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
pink = 255,20,147
turquoise = 72,209,204

# Define colour list
colours = [red, green, blue, yellow, pink, turquoise]

while True:
    for j in colours:
        for i in range(15):
            strip[i] = (j)
            
            # Sets speed of colour chaser
            time.sleep(0.1)

            # Send the data to the strip
            strip.write()

