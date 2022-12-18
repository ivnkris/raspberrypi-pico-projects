# Imports
from machine import Pin
import time

# set up button on GPIO pin and set 3.3v pin to 0v with PULL DOWN
button1 = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True:
    # prevent multiple firings with 1 button press
    time.sleep(0.2)
    
    if button1.value() == 1:
        print("Button 1 pressed")