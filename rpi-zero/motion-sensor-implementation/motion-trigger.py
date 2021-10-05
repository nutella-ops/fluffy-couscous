#!/usr/bin/python3

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

# give pin numbers a name
led = 12
pirSensor = 20

# I/O definitions
gpio.setup(led, gpio.OUT) # phys 32
gpio.setup(pirSensor, gpio.IN) # phys 38
ledOn = gpio.output(led, True)
ledOff = gpio.output(led, False)
motionData = gpio.input(pirSensor)

while True:
	if motionData == True:
		ledOn
	else:
		ledOff