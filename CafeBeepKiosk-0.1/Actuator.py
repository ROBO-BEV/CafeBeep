#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-04-29"
__doc__ =     "Actuator Class to operate at least 8 servos & 2 motors at once"

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

DEBUG = True

# Actuator "forward" direction constants
CCW = -1  # Counter-Clockwise
CW = 1    # Clockwise

# Pin value constants
LOW =  0
HIGH = 1
NO_WIRE = -1
VCC = -2
GND = -3
DATA1 = -4

# Raspberry Pi B+ refernce pin constants as defined in ???rc.local script???
NUM_GPIO_PINS = 8                       #Outputs: GPO0 to GPO3 Inputs: GPI0 to GPI3
MAX_NUM_A_OR_B_PLUS_GPIO_PINS = 40      #Pins 1 to 40 on Raspberry Pi A+ or B+ or ZERO W
MAX_NUM_A_OR_B_GPIO_PINS = 26           #Pins 1 to 26 on Raspberry Pi A or B
NUM_OUTPUT_PINS = 4                     #This software instance of Raspberry Pi can have up to four output pins
NUM_INPUT_PINS = 4                      #This software instance of Raspberry Pi can have up to four input pins

class Actuator:

	# Class attributes that can be accessed using ActuatorControl.X (not actuatorcontrol.X)
	MAX_NUM_OF_SERVOS =  8		# Circular servos
	MAX_NUM_OF_MOTORS =  8		# Circular motors
	MAX_NUM_OF_LINEAR_ACT =  8  	# Linear actuators

	currentNumOfActuators = 0

	wires = [NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE]

	##
	# Constructor to initialize an Actutator object, which can be a Servo(), Motor(), or Relay()
	#
	# @self - ???
	# @pins[] - Array that holds pins being used by Pi 3 to control an actuator
	# @actuatorID - Assigned ID number via incremented interger currentNumOfActuators Class variable
	# @partNumber - Vendor part number string variable (e.g. Seamuing MG996R)
	# @direction - Set counter-clockwise (CCW) or clockwise (CW) as the forward direction
	#
	# return NOTHING
	##
	def __init__(self, wires, actuatorID, partNumber, direction):
		# https://stackoverflow.com/questions/14301967/bare-asterisk-in-function-arguments/14302007#14302007
		# https://gpiozero.readthedocs.io/en/stable/api_output.html
		for i in wires:
			self.wires[i] = wires[i] #TODO: How do I make sure self.pins[] is the correct size before using
		self.actuatorID = actuatorID
		self.partNumber = partNumber
		self.direction = direction
		self.currentNumOfActuators += 1

		if(DetermineActuatorType(wires) == "Servo"):
			DebugPrint("Creating Servo Actuator Object")
			#self.actuatorType = Servo(wires[0], *, initial_value="0", min_pulse_width="1/1000", max_pulse_width="2/1000", frame_width="20/1000", pin_factory="None")
		elif(DetermineActuatorType(wires) == "Motor"):
			DebugPrint("Creating Motor Actuator Object")
			#self.actuatorType = Motor(wires[0], wires[1], *, pwm="true", pin_factory="None")

	def DebugPrint(stringToPrint):
		if(DEBUG):
			print(stringToPrint)
		else:
			#DO NOTHING AND PRINT NEW LINE
			print("/n")

	def DetermineActuatorType(wires):
		numOfWiresUsed = 0
		for i in pins:
			if(wires[i] != NO_WIRE):
				numOfWiresUsed +=1
		if(numOfWiresUsed == 1):
			return "Servo"
		elif(numOfWiresUsed == 2):
			return "Motor"
		elif(numOfWiresUsed == 4):
			return "TODO"

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
	Actuator.wires = [VCC, 1, NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE, NO_WIRE]
	cupSepServo1 = Actuator(Actuator.wires, currentNumOfActuators, "MG996R", CW)

	print("END MAIN")
