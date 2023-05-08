from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time

# Set up I2C
i2c = I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Short delay to stop I2C falling over
time.sleep(1)

# Set up display with correct size (128 x 32)
display = SSD1306_I2C(128, 32, i2c)

# Set up light sensor
lightsensor = ADC(Pin(26))

while True:
    time.sleep(0.5)
    
    # Read sensor value, turn it into a percentage and round to 1 decimal
    light = round((lightsensor.read_u16()) / 65535 * 100, 1)
    
    print(light)
    
    # Clear the display
    display.fill(0)
    
    # Write light reading to display
    display.text("Light level:", 0, 0)
    display.text((str(light) + "%"), 0, 12)
    
    # Update the display
    display.show()