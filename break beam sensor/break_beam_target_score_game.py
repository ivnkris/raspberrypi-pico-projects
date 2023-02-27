from machine import Pin, PWM
import time, sys

# Set up the break beam pin
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up the buzzer
buzzer = PWM(Pin(13))
buzzer.freq(1000)
buzzer.duty_u16(0)

# Set up LEDs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Initiate game variables
starttime = 0
timecheck = 0
scorecounter = 0
state = 0
targetscore = 100

print("Game starts after the beep!")

# Long beep signals game start
buzzer.duty_u16(10000)
time.sleep(2)
buzzer.duty_u16(0)

print("GO!")
print("-----------------------------")

# Store start time in epoch time
starttime = time.time()

while True:
    time.sleep(0.0001)
    
    # Check the elapsed seconds
    timecheck = time.time() - starttime
    
    if timecheck >= 30: #if 30 or more seconds passed
        
        # LEDs off
        red.value(0)
        amber.value(0)
        green.value(0)
        
        # Beep to signal game end
        buzzer.duty_u16(10000)
        time.sleep(0.2)
        buzzer.duty_u16(0)
        
        print("-----------------------------")
        print("GAME OVER! YOU LOST :(")
        print("The target was: ", targetscore, ". You scored: ", scorecounter)
        print("-----------------------------")
        
        # Exit program
        sys.exit()
        
    elif scorecounter >= targetscore: #If player hit the target score
        # LEDs off
        red.value(0)
        amber.value(0)
        green.value(0)
        
        # Beep to signal game end
        buzzer.duty_u16(10000)
        time.sleep(0.2)
        buzzer.duty_u16(0)
        
        print("-----------------------------")
        print("YOU WON!")
        print("You took ", timecheck, " seconds.")
        print("-----------------------------")
        
        sys.exit()
        
    elif state == 0 and beam.value() == 0: #if beam was broken increase score
        scorecounter += 1
        state = 1
        
        print("SCORE: ", scorecounter, "/", targetscore)
        print("TIME REMAINING: ", (30 - timecheck))
        
        if scorecounter < (targetscore / 100 * 33): #if target score less than 33%
            # Red LED on
            red.value(1)
            amber.value(0)
            green.value(0)
            
        elif (targetscore / 100 * 33) < scorecounter < (targetscore / 100 * 66):
            # Amber LED on
            red.value(0)
            amber.value(1)
            green.value(0)
            
        elif scorecounter > (targetscore / 100 * 66):
            # Green LED on
            red.value(0)
            amber.value(0)
            green.value(1)
            
    elif state == 1 and beam.value() == 1: #when beam restored change back state
        state = 0
