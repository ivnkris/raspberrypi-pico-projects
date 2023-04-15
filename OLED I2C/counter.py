from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# Set up I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# Short delay to stop I2C falling over
time.sleep(1)

# Define the display and size (128 x 32)
display = SSD1306_I2C(128, 32, i2c)

counter = 0

while True:
    # Clear the display
    display.fill(0)

    print(counter) # Print the current count to the console

    # Write 3 lines of text to the display
    display.text("The endless",0,0)
    display.text("Counter!",0,12)
    display.text(str(counter),0,24)

    # Update the display
    display.show()
    
    # Short delay
    time.sleep(0.1)
    
    # Increase count
    counter += 1

