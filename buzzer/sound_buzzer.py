# Imports
from machine import Pin, PWM
import time

# set up the buzzer pin
buzzer = PWM(Pin(13))

# set PWM duty for volume
buzzer.duty_u16(10000)

# set PWM frequency for tone
buzzer.freq(1000)
time.sleep(1)

# set PWM frequency for lower tone
buzzer.freq(500)
time.sleep(1)

# turn volume to zero
buzzer.duty_u16(0)