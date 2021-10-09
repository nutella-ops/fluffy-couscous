#!/usr/bin/python3

import RPi.GPIO as gpio, time, os

gpio.setmode(gpio.BCM)

# Named the Pins (BCM referenced)
languageSelect = 12
pirSensor = 20
ledGreen = 8
ledYellow = 10

# Time Definitions
calibDelay = 45	# suggested calibration times {min. = 30 seconds, max. = 60} ideally, there should be as little movement as possible during calibration 
preDelay = 2	# delay before audio starts
postDelay = 40	# delay before audio can start again
delayCounter = 45 # calibration delay stored in a variable to be counted

# I/O definitions
gpio.setup(languageSelect, gpio.IN) # phys 32
gpio.setup(pirSensor, gpio.IN) # phys 38
gpio.setup(ledGreen, gpio.OUT)
gpio.setup(ledYellow, gpio.OUT)

# Setup Dialog
def tenSecond(pin):
		gpio.output(pin, True)
		time.sleep(0.5)
		gpio.output(pin, False)

print("Calibrating...")
if delayCounter != 0:
	while calibDelay <= 10:
		tenSecond(ledGreen)
		tenSecond(ledYellow)
	delayCounter -= 1
gpio.output(ledGreen, False)
gpio.output(ledYellow, False)
print("Calibration Complete.")

# Named the language switch positions
left = False
right = True

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