import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

delay = 0.005

while True:
    for i in range(1, 255, 1):
        strip.fill((i,0,50))
        strip.write()
        time.sleep(delay)
    
    for i in range(255, 1, -1):
        strip.fill((i,0,50))
        strip.write()
        time.sleep(delay)