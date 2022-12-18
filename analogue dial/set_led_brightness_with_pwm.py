# Imports
from machine import ADC, Pin, PWM
import time

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up the LEDs with PWM
red = PWM(Pin(18))
amber = PWM(Pin(19))
green = PWM(Pin(20))

# Set the PWM frequency
red.freq(1000)
amber.freq(1000)
green.freq(1000)

reading = 0

while True:
    # Read potentiometer value
    reading = potentiometer.read_u16()
    print(reading)
    
    # Set the LEDs duty cycle to potentiometer reading
    red.duty_u16(reading)
    amber.duty_u16(reading)
    green.duty_u16(reading)
    
    time.sleep(0.01)
