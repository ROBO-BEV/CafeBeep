#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-04-29"
__doc__ =     "Actuator Control Class to operate at least 8 servos & 2 motors at once"

# https://gpiozero.readthedocs.io/en/stable/installing.html
# https://gpiozero.readthedocs.io/en/stable/
# https://gpiozero.readthedocs.io/en/stable/api_output.html
# https://gpiozero.readthedocs.io/en/stable/api_input.html
# https://www.adafruit.com/product/2348
# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software
# https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/circuitpython-raspi
# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi

#from gpiozero import Motor, Servo, pi_info
#from gpiozero import LED, Button, PingServer  # Allow control of GPIO pins and check status on IP address on network
#from gpiozero.tools import all_values, negated, sin_values
#from gpiozero import Energenie, TimeOfDay

from datetime import time
from time import sleep

from signal import pause          # Allow control of program execution with pasues

# Actuator direction constants 
BACKWARDS = -1
FORWARD = 1

# Pin value constants
LOW =  0
HIGH = 1
NO_PIN = -1

# Raspberry Pi B+ refernce pin constants as defined in ???rc.local script???
NUM_GPIO_PINS = 8                       #Outputs: GPO0 to GPO3 Inputs: GPI0 to GPI3
MAX_NUM_A_OR_B_PLUS_GPIO_PINS = 40      #Pins 1 to 40 on Raspberry Pi A+ or B+ or ZERO W
MAX_NUM_A_OR_B_GPIO_PINS = 26           #Pins 1 to 26 on Raspberry Pi A or B
NUM_OUTPUT_PINS = 4                     #This software instance of Raspberry Pi can have up to four output pins
NUM_INPUT_PINS = 4                      #This software instance of Raspberry Pi can have up to four input pins

class ActuatorControl:

	# Class attributes that can be accessed using ActuatorControl.X (not actuatorcontrol.X)
	MAX_NUM_OF_SERVOS =  8
	currentNumOfActuators = 0
	pins = [NO_PIN, NO_PIN, NO_PIN, NO_PIN]

	##
	# Consctructor to initialize  ActutatorControl objects
	#
	# @self - ???
	# @pins - Array that holds pins being used by Pi 3 to control an actuator
	# @actuatorID - Assigned interger ID number via incremented currentNumOfActuators Class variable
	# @partNumber - Vendor part number (e.g. Seamuing MG996R)
	# @direction - If NEGATIVE counter-clockwise is the forward direction, otherwise clockwise is forward direction
	#
	# return NOTHING
	##
	def __init__(self, pins, actuatorID, partNumber, direction):
		for i in pins:
			self.pins[i] = pins[i] #TODO: How do I make sure self.pins[] is the correct size before using
		self.actuatorID = actuatorID
		self.partNumber = partNumber
		self.direction = direction
		self.currentNumOfActuators += 1

	##
	# Run an actuator for a given number of milliseconds at percentage of max speed in FORWARD or BACKWARDS direction
	#
	# @actuatorID - Assigned interger ID number via incremented currentNumOfActuators Class variable
	# @partNumber - Vendor part number (e.g. Seamuing MG996R)
	# @direction - If NEGATIVE counter-clockwise is the forward direction, otherwise clockwise is forward direction
	#
	# return NOTHING
	##
	def Run(duration, speed, direction):
		print("Run function started!")

		self.enable()
		if(direction == FORWARD):
			self.forward(speed)
		else:
			self.reverse(speed)
		time.sleep(duration)
		self.disable()

		print("Run function completed!")

	def SetPosition(percentage):
		if(percentage == 0):
			print("TEST")
		elif(percentage == 10):
			print("TEST")
		elif(percentage == 25):
			print("TEST")
		elif(percentage == 50):
			print("TEST")
		elif(percentage == 75):
			print("TEST")
		elif(percentage == 100):
			print("TEST")
		else:
			print("TEST")

	def GetPosition():
		return self.value

	def isActive():
		return self.isActive


	def SetAngle(angle):
		print("TEST")


if __name__ == "__main__":

	currentNumOfActuators = 0
	pins = [1, NO_PIN, NO_PIN, NO_PIN]
	cupSepServo1 = ActuatorControl(pins, currentNumOfActuators, "MG996R", FORWARD)

	print("END MAIN")
