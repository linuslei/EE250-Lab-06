import time
import grovepi
from grove_rgb_lcd import *

# Setting up the Rotary Angle Sensor
potentiometer = 0
lcd = 3
grovepi.pinMode(lcd, "OUTPUT")
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

setRGB(0, 128, 64)

while True:
    # Read sensor value from potentiometer
    sensor_value = grovepi.analogRead(potentiometer)
    # Calculate voltage
    range_ref = sensor_value

    # Measure Ultrasound range
    measured_range = grovepi.ultrasonicRead(ultrasound)
    old_measured_range = 0
    old_range = 0

    # Print to Screen
    if (measured_range != old_measured_range) or (range_ref != old_range):
        if measured_range > range_ref:
            setText_norefresh(str(range_ref)+ "cm \n Range: " + str(measured_range) + "cm")
        else:
            setText_norefresh(str(range_ref)+ "cm OBJ PRES\n Range: " + str(measured_range) + "cm")
    old_range = range_ref
    old_measured_range = measured_range
