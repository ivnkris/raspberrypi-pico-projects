# Imports
from machine import Pin
import time

# Set up PIR pin with pull down
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

print("Warming up...")

time.sleep(10) # Delay to allow sensor to baseline environment

print("Sensor ready!")

while True:
    time.sleep(0.01)
    
    if pir.value() == 1: # If PIR detects movement
        print("I SEE YOU!")
        
        time.sleep(5) # Wait before looking for more movement
        
        print("Sensor active")