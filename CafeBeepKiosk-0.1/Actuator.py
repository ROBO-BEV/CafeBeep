#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-01"
__doc__ =     "Actuator Class to operate at least 8 servos & 2 motors at once with latency less then 100 ms"

# https://gpiozero.readthedocs.io/en/stable/installing.html
# https://gpiozero.readthedocs.io/en/stable/
# https://gpiozero.readthedocs.io/en/stable/api_output.html
# https://gpiozero.readthedocs.io/en/stable/api_input.html
# https://www.adafruit.com/product/2348
# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software
# https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/circuitpython-raspi
# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi

#TODO
#from gpiozero import Motor, Servo, pi_info

# Allow control of GPIO pins and check status on IP address on network
#from gpiozero import LED, Button, PingServer

#TODO
#from gpiozero.tools import all_values, negated, sin_values

#TODO
#from gpiozero import Energenie, TimeOfDay

from datetime import time	# TODO
from time import sleep		# TODO

from signal import pause       	# Allow control of program execution with pasues

# Constant to use to toggle debug print statements ON and OFF
DEBUG = True

# Actuator "forward" direction constants
CCW = -1  		# Counter-Clockwise
CW = 1    		# Clockwise
SERVO_SLACK = 0.2	# Positional accuaracy slack for servo so that control system does not go crazy

# Pin value constants
LOW =  0
HIGH = 1

# Wire value constants (interger values don't really matter, but are easy to loop thru)
NO_PIN = 0  #TODO This constant may not be needed :)
NO_WIRE = -1
VCC = -2
GND = -3
PWR = -4
SIG_1 = -5
SIG_2 = -6

# Raspberry Pi B+ refernce pin constants as defined in ???rc.local script???
NUM_GPIO_PINS = 8                       # Outputs: GPO0 to GPO3 Inputs: GPI0 to GPI3
MAX_NUM_A_OR_B_PLUS_GPIO_PINS = 40      # Pins 1 to 40 on Raspberry Pi A+ or B+ or ZERO W
MAX_NUM_A_OR_B_GPIO_PINS = 26           # Pins 1 to 26 on Raspberry Pi A or B
NUM_OUTPUT_PINS = 4                     # This software instance of Raspberry Pi can have up to four output pins
NUM_INPUT_PINS = 4                      # This software instance of Raspberry Pi can have up to four input pins

class Actuator:

	# Class attributes that can be accessed using ActuatorControl.X (not actuatorcontrol.X)
	MAX_NUM_OF_SERVOS = 8		# Circular servos
	MAX_NUM_OF_MOTORS = 2		# Circular motors
	MAX_NUM_OF_LINEAR_ACT = 4  	# Linear actuators

	currentNumOfActuators = 0

	wires = [NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE]

	##
	# Constructor to initialize an Actutator object, which can be a Servo(), Motor(), or Relay()
	#
	# @self - TODO
	# @type - Single String character to select type of actuator to create (S=Servo, M=Motor, R=Relay)
	# @wires[] - Array to document wires / pins being used by Pi 3 to control an actuator
	# @partNumber - Vendor part number string variable (e.g. Seamuing MG996R)
	# @direction - Set counter-clockwise (CCW) or clockwise (CW) as the forward direction
	#
	# return NOTHING
	##
	def __init__(self, type, wires, partNumber, direction):
		for i in wires:
			self.wires[i] = wires[i]
		self.type = type
		self.actuatorID = currentNumOfActuators	# Auto-incremented interger Class variable
		self.partNumber = partNumber
		self.direction = direction
		self.currentNumOfActuators += 1

		#https://gist.github.com/johnwargo/ea5edc8516b24e0658784ae116628277
		# https://gpiozero.readthedocs.io/en/stable/api_output.html
		# https://stackoverflow.com/questions/14301967/bare-asterisk-in-function-arguments/14302007#14302007
		if(type == "S"):
			#self.actuatorType = Servo(wires[0], initial_value=0, min_pulse_width=1/1000, max_pulse_width=2/1000, frame_width=20/1000, pin_factory=None)
			self.actuatorObject = gpiozero.Servo(wires[0])
		elif(type == "M"):
			#self.actuatorType = Motor(wires[0], wires[1], pwm=true, pin_factory=None)
			self.actuatorObject = gpiozero.Motor(wires[0], wires[1])
		elif(type == "R"):
			#self.actuatorObject = gpiozero.OutputDevice(wired[0], active_high=False, initial_value=False)
			self.actuatorObject = gpiozero.OutputDevice(wires[0])
		else:
			DebugPrint("INVALID Actutator Type, please use S, M, R as first parameter to Actuator() Object")

	##
	# Calls standard Python 3 print("X") statement if DEBUG global variable is TRUE
	#
	# return NOTHING
	##
	def DebugPrint(stringToPrint):
		if(DEBUG):
			print(stringToPrint)
		else:
			print("/n") # PRINT NEW LINE


	##
	# Run an actuator for a given number of milliseconds at percentage of max speed in FORWARD or BACKWARDS direction
	#
	# @duration - TODO
	# @newPosition - New position between -1 and 1 that  actuator should move to
	# @speed - TODO
	# @direction - Set counter-clockwise (CCW) or clockwise (CW) as the forward direction
	#
	# return NOTHING
	##
	def Run(duration, newPosition, speed, direction):
		print("Run function started!")

		if(type == "S"):
			currentPosition = self.value
			if(currentPosition < (newPosition - SERVO_SLACK)):
				self.max() #TODO THIS MAY NOT STOP AND GO ALL THE WAY TO MAX POS
			elif(currentPosition > (newPosition - SERVO_SLACK)):
				self.min() #TODO THIS MAY NOT STOP AND GO ALL THE WAY TO MIN POS
			else:
				# NEAR to new position DO NOTHING
				self.dettach()
		elif(type == "M"):
			DebugPrint("Write motor control code")

			self.enable()
			currentPosition = self.value
			while(currentPosition != newPosition):
				if(direction == FORWARD):
					self.forward(speed)
				else:
					self.reverse(speed)
				currentPosition = self.value

			time.sleep(duration)
			self.disable()

		elif(type == "R"):
			DebugPrint("Write relay control code")
		else:
			DebugPrint("INVALID Actutator Type, please use S, M, R as first parameter to Actuator() Object")

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
	pins = [PWR, GND, 1, GND, SIG_1, SIG_2]
	cupSepServo1 = Actuator("S", pins, "MG996R", CW)

	print("END MAIN")
