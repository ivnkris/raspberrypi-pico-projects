import time
from machine import Pin, ADC
from neopixel import NeoPixel

# Define the strip Pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Set up the potentiometer to ADC Pin 26
potentiometer = ADC(Pin(26))

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
            
            # Read the potentiometer and use reading for delay
            delay = potentiometer.read_u16() / 50000
            time.sleep(delay)

            # Send the data to the strip
            strip.write()


