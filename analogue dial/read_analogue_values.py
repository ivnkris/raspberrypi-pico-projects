# Imports
from machine import ADC, Pin
import time

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

while True:
    # Read and print the potentiometer value
    print(potentiometer.read_u16())
    
    time.sleep(1)