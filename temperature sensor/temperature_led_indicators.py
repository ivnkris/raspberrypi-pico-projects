import onewire, ds18x20, time
from machine import Pin

# Set up LEDs
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Set up the ds18x20 sensor
SensorPin = Pin(26, Pin.IN)
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
roms = sensor.scan()

while True:
    sensor.convert_temp() # To centigrade
    time.sleep(2)
    
    for rom in roms:
        reading = sensor.read_temp(rom)
        print(reading, "°C")
        time.sleep(5)

        if reading <= 18:
            red.value(1)
            amber.value(0)
            green.value(0)
        elif 18 < reading < 22:
            red.value(0)
            amber.value(1)
            green.value(0)
        else:
            red.value(0)
            amber.value(0)
            green.value(1)