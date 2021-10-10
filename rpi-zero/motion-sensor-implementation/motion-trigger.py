#!/usr/bin/python3

import RPi.GPIO as gpio, time, os

# Use BCM numbers to reference pins
gpio.setmode(gpio.BCM)

# Audio File Definitions
deutsch = 'full-deutsch.wav'
english = 'full-english.wav' 

# Named the Pins (BCM referenced)
languageSelect = 12
pirSensor = 20
ledRed = 23 # phys 16
ledGreen = 24 # phys 18

# Time Definitions
calibTime = 4	# suggested calibration times {min. = 30 seconds, max. = 60} ideally, there should be as little movement as possible during calibration 
preDelay = 3	# delay before audio starts
retrigDelay = 4	# delay before audio can start again

# Calibration Functon
def calib(t):
	while t > 0:
		time.sleep(1)
		t -= 1

# I/O definitions
gpio.setup(languageSelect, gpio.IN) # phys 32
gpio.setup(pirSensor, gpio.IN) # phys 38
gpio.setup(ledGreen, gpio.OUT)
gpio.setup(ledRed, gpio.OUT)

# Start-up Conditions
gpio.output(ledRed, False)
gpio.output(ledGreen, False)


### MAIN PROGRAM ###

# Initalization Display
gpio.output(ledRed, True)
print("Calibrating...")
calib(calibTime)
print("Calibration Complete.")
gpio.output(ledRed, False)
gpio.output(ledGreen, True)

# Named the language switch positions
left = False
right = True

while True:
	if gpio.input(pirSensor) == True:
		if gpio.input(languageSelect) == left:
			gpio.output(ledGreen, True)
			time.sleep(preDelay)	# 2 second delay in audio output so audio doesn't start immedately on movement
			gpio.output(ledGreen, False)
			gpio.output(ledRed, True)	# turn red led on to inidicate triggering is inactive 
			os.system('aplay /home/pi/' + deutsch)
			time.sleep(retrigDelay)	# delay to prevent immediate retriggering
			gpio.output(ledRed, False)	# turn red led on to inidicate triggering is active 
			gpio.output(ledGreen, True)
		
		if gpio.input(languageSelect) == right:
			gpio.output(ledGreen, True)
			time.sleep(preDelay)	# 2 second delay in audio output so audio doesn't start immedately on movement
			gpio.output(ledGreen, False)
			gpio.output(ledRed, True)	# turn red led on to inidicate triggering is inactive 
			os.system('aplay /home/pi/' + english)
			time.sleep(retrigDelay)	# delay to prevent immediate retriggering
			gpio.output(ledRed, False)	# turn red led on to inidicate triggering is active 
			gpio.output(ledGreen, True)