# imports
from machine import Pin, PWM, ADC
import time

# set up buzzer and potentiometer
potentiometer = ADC(Pin(27))
buzzer = PWM(Pin(13))

# initialize potentiometer reading variable
reading = 0

while True:
    time.sleep(0.01)
    
    reading = potentiometer.read_u16()
    print(reading)
    
    # set buzzer tone
    buzzer.freq(500)
    
    # set buzzer volume
    buzzer.duty_u16(reading)