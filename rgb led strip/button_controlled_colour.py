import time
from machine import Pin
from neopixel import NeoPixel

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
strip = NeoPixel(Pin(28), 15)

# Colour variables
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
pink = 255,20,147
turquoise = 72,209,204

colours = [red, green, blue, yellow, pink, turquoise]

index = 0
indexlength = len(colours) - 1

while True:
    time.sleep(0.4)
    
    if button() == 1:
        if index < indexlength:
            index = index + 1
        else:
            index = 0
        
        strip.fill(colours[index])
        strip.write()
