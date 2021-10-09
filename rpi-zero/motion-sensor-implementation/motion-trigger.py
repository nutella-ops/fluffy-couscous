#!/usr/bin/python3

import RPi.GPIO as gpio, time, os

gpio.setmode(gpio.BCM)

# Name the Pins
languageSelect = 12
pirSensor = 20

# Time Definitions
calibDelay = 45	# min. suggested = 30 seconds, max. suggested = 60
preDelay = 2	# delay before audio starts
postDelay = 40	# delay before audio can start again

# I/O definitions
gpio.setup(languageSelect, gpio.IN) # phys 32
gpio.setup(pirSensor, gpio.IN) # phys 38
left = False
right = True


# Setup Dialog
print("Calibrating...")
time.sleep(calibDelay)
print("Calibration Complete.")

while True:
	if gpio.input(pirSensor) == True:
		if gpio.input(languageSelect) == left:
			time.sleep(preDelay)	# 2 second delay in audio output so audio doesn't start immedately on movement 
			os.system('aplay /home/pi/full-deutsch.wav')
			time.sleep(postDelay)	# 40 second delay to prevent immediate retriggering
		
		if gpio.input(languageSelect) == right:
			time.sleep(preDelay)	# 2 second delay in audio output so audio doesn't start immedately on movement 
			os.system('aplay /home/pi/full-english.wav')
			time.sleep(postDelay)	# 40 second delay to prevent immediate retriggering