#!/usr/bin/python3

import RPi.GPIO as gpio, time, os

gpio.setmode(gpio.BCM)

# Named the Pins (BCM referenced)
languageSelect = 12
pirSensor = 20
ledRed = 23 # phys 16
ledGreen = 24 # phys 18

# Time Definitions
calibTotal = 4	# suggested calibration times {min. = 30 seconds, max. = 60} ideally, there should be as little movement as possible during calibration 
preDelay = 3	# delay before audio starts
postDelay = 4	# delay before audio can start again
calibRemain = 2 # the length of led indication in seconds
calibMain = abs(calibTotal - calibRemain) # setting aside 10 seconds for led indication, assigning the remainder as the calibMain

# I/O definitions
gpio.setup(languageSelect, gpio.IN) # phys 32
gpio.setup(pirSensor, gpio.IN) # phys 38
gpio.setup(ledGreen, gpio.OUT)
gpio.setup(ledRed, gpio.OUT)

# Setup Dialog
def blink(pin):
		gpio.output(pin, True)
		time.sleep(1)
		gpio.output(pin, False)

def ledIndicator(time, color):
	if time <= 10:
		while time > 0:
			blink(color)
			time -= 1

# Start-up Conditions
gpio.output(ledRed, False)
gpio.output(ledGreen, False)

### MAIN PROGRAM ###

# Initalization Display
print("Calibrating...")
gpio.output(ledRed, True)

while calibMain > 0:
       time.sleep(1)
       print(calibMain)
       calibMain -= 1
print("Calibration Complete.")
gpio.output(ledRed, False)

# gpio.output(ledGreen, True)

# Named the language switch positions
left = False
right = True
# gpio.output(ledGreen, False)	# turn off led to indicate trigger
while True:
	if gpio.input(pirSensor) == True:
		if gpio.input(languageSelect) == left:
			time.sleep(preDelay)	# 2 second delay in audio output so audio doesn't start immedately on movement
			gpio.output(ledRed, True)	# turn red led on to inidicate triggering is inactive 
			os.system('aplay /usr/share/sounds/alsa/Front_Center.wav')
			gpio.output(ledRed, False)
			# time.sleep(postDelay)	# delay to prevent immediate retriggering
			ledIndicator(calibRemain, ledRed)	# flash led for for (delayRemain) seconds 
		
		if gpio.input(languageSelect) == right:
			time.sleep(preDelay)	# 2 second delay in audio output so audio doesn't start immedately on movement
			gpio.output(ledRed, True)	# turn red led on to inidicate triggering is inactive 
			os.system('aplay /usr/share/sounds/alsa/Rear_Center.wav')
			gpio.output(ledRed, False)
			# time.sleep(postDelay)	# delay to prevent immediate retriggering
			ledIndicator(calibRemain, ledRed)	# flash led for for (delayRemain) seconds 