# Imports
from machine import Pin
import time

# set up buttons on GPIO pins and set 3.3v pin to 0v with PULL DOWN
button1 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# set up LEDs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)


while True:
    # prevent multiple firings with 1 button press
    time.sleep(0.2)
    
    # toggle LEDs on and off
    if button1.value() == 1:
        print("Button 1	pressed")
        red.toggle()
        amber.toggle()
        green.toggle()
        

