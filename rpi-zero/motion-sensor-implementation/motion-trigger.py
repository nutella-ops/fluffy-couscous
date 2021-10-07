#!/usr/bin/python3

import RPi.GPIO as gpio, time, os

gpio.setmode(gpio.BCM)

# give pin numbers a name
SPDT = 12
pirSensor = 20

# I/O definitions
gpio.setup(SPDT, gpio.IN) # phys 32
gpio.setup(pirSensor, gpio.IN) # phys 38

while True:
	if gpio.input(pirSensor) == True:
		if gpio.input(SPDT) == False:
			time.sleep(2)	# 2 second delay in audio output so audio doesn't start immedately on movement 
			os.system('aplay /home/pi/full-deutsch.wav')
			time.sleep(40)	# 40 second delay to prevent immediate retriggering
		
		if gpio.input(SPDT) == True:
			time.sleep(2)	# 2 second delay in audio output so audio doesn't start immedately on movement 
			os.system('aplay /home/pi/full-english.wav')
			time.sleep(40  )	# 40 second delay to prevent immediate retriggering