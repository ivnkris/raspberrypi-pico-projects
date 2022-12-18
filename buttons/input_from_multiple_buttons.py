# Imports
from machine import Pin
import time

# set up buttons on GPIO pins and set 3.3v pin to 0v with PULL DOWN
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True:
    # prevent multiple firings with 1 button press
    time.sleep(0.2)
    
    if button1.value() == 1:
        print("Button 1	pressed")
        
    elif button2.value() == 1:
        print("Button 2	pressed")
    
    elif button3.value() == 1:
        print("Button 3	pressed")