# Imports
from machine import ADC, Pin
import time

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up the red LED
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

mydelay = 0

while True:
    # Update delay with potentiometer reading
    mydelay = potentiometer.read_u16() / 65000
    print(mydelay)
    
    # LEDs on for variable delay period
    red.value(1)
    amber.value(1)
    green.value(1)
    time.sleep(mydelay)
    
    # LEDs off for variable delay period
    red.value(0)
    amber.value(0)
    green.value(0)
    time.sleep(mydelay)