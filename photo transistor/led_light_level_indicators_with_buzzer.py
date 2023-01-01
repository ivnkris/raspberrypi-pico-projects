#Imports
from machine import ADC, Pin, PWM
import time

# Set up LED pins
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Define ADC Pin for light sensor
lightsensor = ADC(Pin(26))

# set up buzzer
buzzer = PWM(Pin(13))

# define note
note = 350

# define volume
volume = 16500

def playtone(note, vol, delay1, delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)

while True:

    # Read analouge sensor value
    light = lightsensor.read_u16()

    # Turn reading into percentage
    lightpercent = round(light / 65535 * 100, 2)

    print(str(lightpercent) + "%")
    
    # Delay between readings
    time.sleep(1)
    
    if lightpercent <= 25: # If percentage less than equal 25% indicate with red LED
        red.value(1)
        amber.value(0)
        green.value(0)
        
        # play buzzer
        playtone(note, volume, 0.5, 0.2)
        
    elif 25 < lightpercent < 60: # If percentage between 25% and 60% indicate with amber LED
        red.value(0)
        amber.value(1)
        green.value(0)
        
    elif lightpercent >= 60: # If percentage greater than or equal to 60% indicate with green LED
        red.value(0)
        amber.value(0)
        green.value(1)
