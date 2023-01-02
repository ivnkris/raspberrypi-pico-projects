# Imports
from machine import Pin, PWM
import time

# Set up LEDs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Set up the buzzer
buzzer = PWM(Pin(13))
buzzer.duty_u16(0)

# Set up PIR pin with pull down
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

print("Warming up...")
time.sleep(10) # Delay to allow sensor to baseline environment
print("Sensor ready!")

def alarm():
    # Buzzer volume up
    buzzer.duty_u16(10000)
    
    for i in range(5):
        buzzer.freq(5000) # High pitch buzzer
        
        # LEDs on
        red.value(1)
        amber.value(1)
        green.value(1)
        
        time.sleep(1)
        
        buzzer.freq(500) # Low pitch buzzer
        
        # LEDs off
        red.value(0)
        amber.value(0)
        green.value(0)
        
        time.sleep(1)
        
    # Buzzer off
    buzzer.duty_u16(0)

while True:
    time.sleep(0.01)
    
    if pir.value() == 1: # If PIR detects movement
        print("I SEE YOU!")
        
        alarm()
        
        print("Sensor active")
