#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.IN) # phys 32
GPIO.setup(20, GPIO.OUT) # phys 38


led = GPIO.output(20, True)

while True:
	GPIO.output(20, True)
	time.sleep(1)
	GPIO.output(20, False)
	time.sleep(1)

	# motionSensor = GPIO.input(12)
	# if motionSensor == True:
	# 	GPIO.output(20, motionSensor)
