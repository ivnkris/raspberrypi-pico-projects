# Imports
from machine import Pin
import time

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Set up button
button1 = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True:
    # Green ON
    red.value(0)
    amber.value(0)
    green.value(1)
    
    if button1.value() == 1:
        time.sleep(0.5)
    
        # Amber ON
        red.value(0)
        amber.value(1)
        green.value(0)
    
        time.sleep(2)
    
        # Red ON
        red.value(1)
        amber.value(0)
        green.value(0)
    
        # Wait half a second
        time.sleep(7.5)
    
        # Amber ON
        red.value(1)
        amber.value(1)
        green.value(0)
    
        time.sleep(1)
    


