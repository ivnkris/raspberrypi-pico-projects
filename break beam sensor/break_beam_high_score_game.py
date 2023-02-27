from machine import Pin, PWM
import time, sys

# Set up the break beam pin
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up the buzzer
buzzer = PWM(Pin(13))
buzzer.freq(1000)
buzzer.duty_u16(0)

# Initiate game variables
starttime = 0
timecheck = 0
scorecounter = 0
state = 0

print("Game starts after the beep!")

# Long beep signals game start
buzzer.duty_u16(10000)
time.sleep(2)
buzzer.duty_u16(0)

print("GO!")

# Store start time in epoch time
starttime = time.time()

while True:
    time.sleep(0.0001)
    
    # Check the elapsed seconds
    timecheck = time.time() - starttime
    
    if timecheck >= 30: #if 30 or more seconds passed
        print("GAME OVER!")
        
        # Beep to signal game end
        buzzer.duty_u16(10000)
        time.sleep(0.2)
        buzzer.duty_u16(0)
        
        print("YOUR SCORE: ", scorecounter)
        
        # Exit program
        sys.exit()
        
    elif state == 0 and beam.value() == 0: #if beam was broken increase score
        scorecounter += 1
        state = 1
        
        print("SCORE: ", scorecounter)
        print("TIME REMAINING: ", (30 - timecheck))
        
    elif state == 1 and beam.value() == 1: #when beam restored change back state
        state = 0