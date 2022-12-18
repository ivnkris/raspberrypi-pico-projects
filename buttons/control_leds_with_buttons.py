# Imports
from machine import Pin
import time

# set up buttons on GPIO pins and set 3.3v pin to 0v with PULL DOWN
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# set up LEDs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)


while True:
    # prevent multiple firings with 1 button press
    time.sleep(0.2)
    
    if button2.value() == 1 and button3.value() == 1:
        print("Button 2 and 3	pressed")
        green.value(1)
        
    elif button2.value() == 1:
        print("Button 2	pressed")
        amber.value(1)
    
    else:
        red.value(1)
        amber.value(0)
        green.value(0)
