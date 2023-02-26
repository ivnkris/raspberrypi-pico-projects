from machine import Pin
import time

# Set up tilt sensor
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)
tiltcount = 0
state = 0 # State variable set to zero when Pin is LOW

while True:
    time.sleep(0.1)
    if state == 0 and tilt.value() == 1:
        tiltcount += 1
        state = 1 # State variable to 1 when Pin is HIGH
        print("tilts = ", tiltcount)
    if state == 1 and tilt.value() == 0:
        state = 0 # Reset state


