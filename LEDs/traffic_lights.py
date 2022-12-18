# Imports
from machine import Pin
import time

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True:
    
    # Red ON
    red.value(1)
    amber.value(0)
    green.value(0)
    
    # Wait half a second
    time.sleep(2.5)
    
    # Amber ON
    red.value(1)
    amber.value(1)
    green.value(0)
    
    time.sleep(0.5)
    
    # Green ON
    red.value(0)
    amber.value(0)
    green.value(1)
    
    time.sleep(5)
    
    # Amber ON
    red.value(0)
    amber.value(1)
    green.value(0)
    
    time.sleep(0.5)

