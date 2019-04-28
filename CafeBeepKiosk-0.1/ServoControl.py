#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-04-22"
__doc__ =     "Servo Control Class to operate at least 8 servos at once"

# https://gpiozero.readthedocs.io/en/stable/installing.html
# https://gpiozero.readthedocs.io/en/stable/
# https://gpiozero.readthedocs.io/en/stable/api_output.html
# https://gpiozero.readthedocs.io/en/stable/api_input.html
# https://www.adafruit.com/product/2348
# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software
# https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/circuitpython-raspi
# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi

from gpiozero import Motor, Servo, pi_info
from gpiozero import LED, Button, PingServer  # Allow control of GPIO pins and check status on IP address on network
from gpiozero.tools import all_values, negated, sin_values
from gpiozero import Energenie, TimeOfDay

from datetime import time
from time import sleep

from signal import pause          # Allow control of program execution with pasues

class ServoControl:
	MAX_NUM_OF_SERVOS =  8

	def __init__(self, pins, servoID, partNumber, direction):
		for i in pins:
			self.pins[i] = pins[i] #TODO: How do I make sure self.pins[] is the correct size before using
		self.servoID = servoID
		self.partNumber = servoPartNumber
		self.direction = direction


	def Run(duration, direction):
		print("TEST")
	def SetAngle(angle):
		print("TEST")


if __name__ == "__main__":

	led = LED("GPIO17") #OR LED("BCM17"), since all GPIO pin numbers use Broadcom (BCM) numbering by default

	kiosk0 = Energenie(1) 			# TODO What does the 1 mean?
	onTime = TimeOfDay(time(5), time(2)) 	# cafeBEEP normal open 5 AM to 2 AM
	kiosk0.source = onTime


	#TODO: How to use optional & skipped paramaters? cupSepServo1 = Servo(1, ?, 0.3, 1, 2, 20)
	cupSepServo1.isActive
	posCupSepServo1 = cupSepServo1.value

	cupSepServo1.initial_value(0.3) #Default start position as ?0.3?
	cupSepServo1.min_pulse_width(1) #1 ms PWM
	cupSepServo1.min() # Move to min position
	cupSepServo1.mid() # Move to mid position
	cupSepServo1.max() # Move to max position

	#TODO: Servo #2
	cupSepServo2 = Servo(2)

	cupConveyorMotor1 = Motor(3, 4)
	cupConveyorMotor1.enable(5)	 # The GPIO pin that enables the motor. Required for some motor controller boards

	cupConveyorMotor1.forward(0.20)  # Speed 20%
	cupConveyorMotor1.backward(1)    # Speed 100%
	cupConveyorMotor1.pwm(false)	 # If True allow both direction and variable speed control, otherwise just direction

	cupConveyorMotor1.stop()
	isConveyorOn = cupConveyorMotor1.is_active
	currentSpeed = cupConveyorMotor1.value

	relay1 = OutputDevice(6) # Generic GPIO output device with on(), off() toggle() methods
	relay1.on()
	relay1.off()
	relay1.toggle()
	relay1.active_high = True
	relay1State = relay1.value

	relay2 = OutputDevice(6)
	relay3 = OutputDevice(6)
	relay4 = OutputDevice(6)

	#TODO: Motor #2
	#cupConveyorMotor2 = Motor(?, ?)
