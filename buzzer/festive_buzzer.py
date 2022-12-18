# imports
from machine import Pin, PWM
import time

# set up buzzer
buzzer = PWM(Pin(13))

# note library for "jingle bells"
C = 523
D = 587
E = 659
F = 698
G = 784

# volume variable
volume = 16500

def playtone(note, vol, delay1, delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)

# Play the tune
playtone(E, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.5)

playtone(E, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.5)

playtone(E, volume, 0.1, 0.2)
playtone(G, volume, 0.1, 0.2)
playtone(C, volume, 0.1, 0.2)
playtone(D, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 1)

playtone(F, volume, 0.1, 0.2)
playtone(F, volume, 0.1, 0.2)
playtone(F, volume, 0.1, 0.2)
playtone(F, volume, 0.1, 0.2)
playtone(F, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.2)
playtone(E, volume, 0.1, 0.2)

playtone(E, volume, 0.1, 0.1)
playtone(E, volume, 0.1, 0.1)
playtone(G, volume, 0.1, 0.2)
playtone(G, volume, 0.1, 0.2)
playtone(F, volume, 0.1, 0.2)
playtone(D, volume, 0.1, 0.2)
playtone(C, volume, 0.1, 1)

# Duty turns the buzzer off
buzzer.duty_u16(0)