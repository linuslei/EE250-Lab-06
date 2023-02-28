import time
import grovepi
from grove_rgb_lcd import *

# Setting up the Rotary Angle Sensor
potentiometer = 0
led = 5
grovepi.pinMode(led, "OUTPUT")
grovepi.pinMode(potentiometer, "INPUT")
time.sleep(1)
adc_ref = 5
grove_vcc = 5
full_angle = 300

# Setting up the Ultrasonic Sensor
grovepi.set_bus("RPI_1")
ultrasound = 4

# Setting up the LCD
lcd = 0x3f
grovepi.lcdInit(lcd)
grovepi.lcdSetRGB(lcd, 0, 128, 64)

while True:
    # Read sensor value from potentiometer
    sensor_value = grovepi.analogRead(potentiometer)
    # Calculate voltage
    range_ref = sensor_value

    # Measure Ultrasound range
    measured_range = grovepi.ultrasonicRead(ultrasound)

    # Print to Screen
    if measured_range > range_ref:
        setText("Threshold: " + str(range_ref)+ "\n Range: " + str(measured_range) + "cm")
    else:
        setText("Threshold: " + str(range_ref)+ "cm OBJ PRES\n Range: " + str(measured_range) + "cm")

    time.sleep(.5)
