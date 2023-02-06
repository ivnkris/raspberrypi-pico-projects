import onewire, ds18x20, time
from machine import Pin

SensorPin = Pin(26, Pin.IN)
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
roms = sensor.scan()

while True:
    sensor.convert_temp() # To centigrade
    time.sleep(2)
    
    for rom in roms:
        print((sensor.read_temp(rom)), "°C")
        time.sleep(5)