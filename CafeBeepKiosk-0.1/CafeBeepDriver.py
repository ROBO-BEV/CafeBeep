#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-15"
__doc__ =     "Logic to run cafeBEEP kiosk back-end"

# Useful system jazz
import sys, time, traceback, argparse, string


# BEEP BEEP Technologies Inc code
#SHOULD NOT NEED THIS FOR BACK END import UserData         # Store user name, ID, and drink preferences
import Drink            # Store valid BEEP BEEP drink configurations
import Actuator         # Modular plug and play control of motors, servos, and relays


class CafeBeepDriver:


	###
	# Actuate two servos to drop cups into conveyer system
	# NOTE: HARD CODED SERVO OBJECTS
	#
	# @numberOfCups - Number of cups to drop
	# @actuatorObjects - Array of Servo() objects to control
	#
	# return NOTHING
	###
	def dropCup(numberOfCups, actuatorObjects):
		for i in range(1, numOfCups+1)
			actuatorObjects[i].min()		# OLD WAY cupSeparatorServo1.min()
			actuatorObjects[i+1].min()
			time.sleep(1.500) 		# Pause 1500 ms
			actuatorObjects[i].max()		# OLD WAY cupSeparatorServo1.min()
			actuatorObjects[i+1].max()

	###
	# Actuate linear actuators to push cup into user vend port
	# NOTE: HARD CODED LINEAR ACTUATOR OBJECT
	#
	# @actuatorObjects - Array of Relay() / linear actuator objects to control
	#
	# return NOTHING
	###
	def liftCup(actuatorObjects):
		for i for actuatorObjects
			actuatorObjects[i].min()
			time.sleep(1.700) 		# Pause 1700 ms
			actuatorObjects[i].max()

	###
	#
	#
	###
	def actuateMilkMotor(milkType, milkLevel):
		print("TODO")

	###
	#
	#
	###
	def actuateSugarMotor(sugarType, sugarLevel):
		if(Drink.NONE <= sugareLevel and sugarLevel < Drink.MAX_SUGAR_LEVEL):
			actuationTime = sugarLevel / 10  #Units of milliSeconds NEED REAL LIFE TESTING
			if(sugarType == Drink.SIMPLE_SYRUP):
				simpleSyrupSugarMotor.run(actuationTime, ???, 0.5, Actuator.FORWARD)
			elif(sugarType == Drink.CARMEL):
				#time.delay(atuationTIme)
			elif(sugarType == Drink.CHOCOLATE):
				#ONE OF ABOVE METHODS
			else:
				print("INVALID SUGAR TYPE PASSED TO FUNCTION - TRY SIMPLE_SYRUP CONSTANT")
		else:
			print("INVALID SUGAR LEVEL PASSED TO FUNCTION - TRY VALUE 0 TO 8")

	###
	#
	#
	###
	def shiftQueue():
		print("TODO")

if __name__ == "__main__":

	cupSeparatorServo1Pins = [VCC, BCM8, GND]
	cupSeparatorServo1Wires = [VCC, 9, GND]


	currentNumberOfOrders = 0
	numOfOrdersInProgress = 1
	vendQueue[10] = {}

	# DEFINE ALL ACTUATOR OBJECT
	cupSeparatorServo1 = Actuator("S", pins[], "Seamuing MG996R", )
	cupSeparatorServo2 = Actuator("S", )
	
	simpleSyrupSugarMotor =  Actuator("M", )
	carmelSugarMotor =  Actuator("M", )
	chocolateSugarMotor =  Actuator("M", )

	halfHalfMilkMotor =
	??MilkMotor = 
	??MilkMotor = 

	Actuators[12] = {simpleSyrupSugarMotor, ???}

	while(numOfOrdersInProgress < currentNumberOfOrders):
		vendingDrink = vendQueue[0] # vendingDrink is drink currently in process
		if(vendingDrink.getSugarType != NONE):
			actuateSugarMotor(vendingDrink.getSugarType, vendinfDrink.getSugarLevel)

		if(vendingDrink.getMilkType != NONE):
			actuateMilkMotor(vendingDrink.getMilkType, vendinfDrink.getMilkLevel)

		shiftQueue()
