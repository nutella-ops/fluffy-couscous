#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT) # phys 32
GPIO.setup(20, GPIO.IN) # phys 38

def led(logic):
	GPIO.output(12, logic)

while True:
	led(True)
	time.sleep(1)
	led(False)
	time.sleep(1)

	# motionSensor = GPIO.input(12)
	# if motionSensor == True:
	# 	GPIO.output(20, motionSensor)
