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

while True:
	if gpio.input(pirSensor) == True:
		gpio.output(led, True)
	else:
		gpio.output(led, False)