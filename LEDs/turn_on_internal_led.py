from machine import Pin
onboardLED = Pin(25, Pin.OUT)

# switch to 1 to turn on LED
onboardLED.value(0)