# Imports
from machine import ADC, Pin
import time

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up the red LED
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

reading = 0

while True:
    # Update delay with potentiometer reading
    reading = potentiometer.read_u16()
    print(reading)
    time.sleep(0.1)
    
    if reading <= 20000:
        red.value(1)
        amber.value(0)
        green.value(0)
        
    elif 20000 < reading < 40000:
        red.value(0)
        amber.value(1)
        green.value(0)
        
    elif reading >= 40000:
        red.value(0)
        amber.value(0)
        green.value(1)