#!/usr/bin/python3

import RPi.GPIO as gpio, time, os


#####################
### GENERAL SETUP ###
#####################

# Use BCM numbers to reference pins
gpio.setmode(gpio.BCM)

# Audio File Definitions
DE = 'de-bg-remove.wav'
EN = 'en-bg-remove.wav' 

# Named the Pins (BCM referenced)
languageSelect = 12	# phys 32
pirSensor = 20	# phys 38
ledRed = 23 # phys 16
ledGreen = 24 # phys 18

# Time Definitions
startDelay = 5	# seconds before calibration starts
calibTime = 40	# suggested calibration times {min. = 30 seconds, max. = 60} ideally, there should be as little movement as possible during calibration 
preDelay = 3	# seconds before audio starts
retrigDelay = 40	# seconds before audio can start again

# I/O definitions
gpio.setup(languageSelect, gpio.IN) 
gpio.setup(pirSensor, gpio.IN) 
gpio.setup(ledGreen, gpio.OUT)
gpio.setup(ledRed, gpio.OUT)
left = False	# named the switch positions
right = True


############################
### FUNCTION DEFINITIONS ###
############################

# LED Abstraction, Green to Red
def greenToRed():
	gpio.output(ledGreen, False)
	gpio.output(ledRed, True)

# LED Abstraction, Red to Green
def redToGreen():
	gpio.output(ledRed, False)
	gpio.output(ledGreen, True)

# Calibration Functon
def calib(t):
	while t > 0:
		gpio.output(ledRed, True)
		time.sleep(0.5)
		gpio.output(ledRed, False)
		time.sleep(0.5)
		t -= 1

# Initialization Function
def init(t):
	gpio.output(ledRed, True) 
	print("Calibrating...")
	calib(t)
	print("Calibration Complete.")
	gpio.output(ledRed, False)
	gpio.output(ledGreen, True)

# Motion Greeting and Status Indicator
def greeting(language):
	time.sleep(preDelay) # delay in audio output so audio doesn't start immedately on movement
	greenToRed()
	os.system('aplay /home/pi/' + language)
	time.sleep(retrigDelay) # delay to prevent immediate retriggering
	redToGreen()


####################
### MAIN PROGRAM ###
####################

# Start-up Conditions
gpio.output(ledRed, False)
gpio.output(ledGreen, False)

# Start-up Delay
time.sleep(startDelay)

# Initalization Display
init(calibTime)

# Motion Sensor Loop
while True:
	if gpio.input(pirSensor) == True:
		if gpio.input(languageSelect) == left:
			greeting(DE)
		
		if gpio.input(languageSelect) == right:
			greeting(EN)