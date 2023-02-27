from machine import Pin
import time

# Set up beam pin
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

while True:
    time.sleep(0.1)
    
    if beam.value() == 0:
        print("Beam broken!")