import onewire, ds18x20, time
from machine import Pin, PWM

# Set up LEDs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Set up the buzzer
buzzer = PWM(Pin(13))
buzzer.duty_u16(0)

# Set up the ds18x20 sensor
SensorPin = Pin(26, Pin.IN)
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
roms = sensor.scan()

def alarm():
    buzzer.duty_u16(10000)
    
    for i in range(5):
        buzzer.freq(5000)
        red.value(1)
        amber.value(1)
        green.value(1)
        
        time.sleep(0.2)
        
        buzzer.freq(1000)
        red.value(0)
        amber.value(0)
        green.value(0)
        
        time.sleep(0.2)
        
    buzzer.duty_u16(0)

while True:
    sensor.convert_temp() # To centigrade
    time.sleep(2)
    
    for rom in roms:
        reading = sensor.read_temp(rom)
        print(reading, "°C")
        time.sleep(5)

        if reading < 18:
            alarm()
