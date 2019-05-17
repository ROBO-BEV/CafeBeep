#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-17"
__doc__ =     "Logic to run cafeBEEP kiosk back-end"

# Useful system jazz
import sys, time, traceback, argparse, string

# BEEP BEEP Technologies Inc code
#SHOULD NOT NEED THIS FOR BACK END import UserData         # Store user name, ID, and drink preferences
import Drink            # Store valid BEEP BEEP drink configurations
import Actuator         # Modular plug and play control of motors, servos, and relays

# Create a command line parser
parser = argparse.ArgumentParser(prog = "cafeBEEP v2019.0", description = __doc__, add_help=True)
parser.add_argument("-i", "--piIP_Address", type=str, default="192.168.1.135", help="IPv4 address of the cafeBEEP V0 ID1 Raspberry Pi.")
parser.add_argument("-r", "--rx_Socket", type=int, default=30000, help="UDP port / socket number for connected Ethernet device.")
parser.add_argument("-s", "--tx_Socket", type=int, default=30100, help="UDP port / socket number for connected Ethernet device.")
parser.add_argument("-u", "--unit", type=str, default= FIELD_MODE, choices=[TESTING_MODE, FIELD_MODE, PRODUCT_MODE], help="Select boot up mode for BARISTO kiosk.")
parser.add_argument("-t", "--trace", type=int, default=0, help="Program trace level.")
parser.add_argument("-f", "--filename", type=str, default="Update.py", help="Local or cloud software to be loaded on kiosk.")
parser.add_argument("-l", "--loop", type=int, default=0, help="Set to 1 to loop this driver program.")
args = parser.parse_args()

class CafeBeepDriver:

	PRODUCT_MODE = "PRODUCT"        # Final product configuration
	FIELD_MODE  = "FIELD"		# Non-Techanical repair person configuration
	TESTING_MODE = "TESTING"        # Internal developer configuration
	DEBUG_STATEMENTS_ON = True      # Toogle debug statements on and off for this python file

	#Raspberry Pi B+ refernce pin constants as defined in ???rc.local script???
	NUM_PI_GPIO_PINS = 8                  	#Outputs: GPO0 to GPO3 Inputs: GPI0 to GPI3
	MAX_NUM_PI_A_OR_B_PLUS_GPIO_PINS = 40 	#Pins 1 to 40 on Raspberry Pi A+ or B+ or ZERO W
	MAX_NUM_PI_A_OR_B_GPIO_PINS = 26      	#Pins 1 to 26 on Raspberry Pi A or B
	NUM_PI_OUTPUT_PINS = 4                	#This software instance of Raspberry Pi can have up to four output pins
	NUM_PI_INPUT_PINS = 4                 	#This software instance of Raspberry Pi can have up to four input pins
	#UART pins in BCM mode are: 14, 15 /dev/ttyAMA0

	#TODO NVIDIA PINS

	###
	# Actuate two servos to drop cups into conveyer system
	# TODO HARD CODED SERVO OBJECTS?
	#
	# @numberOfCups - Number of cups to drop
	# @actuatorObjects - Array of Servo() objects to control
	#
	# return NOTHING
	###
	def dropCup(numberOfCups, actuatorObjects):
		for i in range(1, numOfCups+1):
			actuatorObjects[i].min()		# OLD WAY cupSeparatorServo1.min()
			actuatorObjects[i+1].min()
			time.sleep(1.500) 			# TODO REAL LIFE TESTING Pause 1500 ms
			actuatorObjects[i].max()		# OLD WAY cupSeparatorServo1.min()
			actuatorObjects[i+1].max()

	###
	# Actuate linear actuators to push cup into onf of the user vend ports
	# NOTE: HARD CODED LINEAR ACTUATOR OBJECT
	#
	# @actuatorObjects - Array of Relay() / linear actuator objects to control
	#
	# return NOTHING
	###
	def liftCup(actuatorObjects):
		for i in actuatorObjects:
			actuatorObjects[i].min()
			time.sleep(1.700) 		# TODO REAL LIFE TESTING Pause 1700 ms
			actuatorObjects[i].max()

	###
	# Actuate peristaltic pump to dispense liquid milk into cup
	#
	# @milkType - Product name of milk add-on to dispense (e.g. HALF_HALF)
	# @milkLevel - Amount of milk units to dispense 1 = 0.25 oz
	#
	# return NOTHING
	###
	def actuateMilkMotor(milkType, milkLevel):
		print("TODO")

	###
	# Actuate peristaltic pump to dispense liquid sugar into cup
	#
	# @sugarType - Product name of sugar add-on to dispense (e.g. SIMPLE_SYRUP)
	# @sugarLevel - Amount of sugar units to dispense 1 = ?? oz
	#
	# return NOTHING
	###
	def actuateSugarMotor(sugarType, sugarLevel):
		if(Drink.NONE <= sugareLevel and sugarLevel < Drink.MAX_SUGAR_LEVEL):
			actuationTime = sugarLevel / Drink.SUGAR_FLOW_RATE  #Units of Seconds based on flow rate per second of pump
			if(sugarType == Drink.SIMPLE_SYRUP):
				print("TODO")
				#simpleSyrupSugarMotor.run(actuationTime, ???, 0.5, Actuator.FORWARD)
			elif(sugarType == Drink.CARMEL):
				print("TODO")
				#time.sleep(actuationTime)
			elif(sugarType == Drink.Vanilla):
				print("TODO")
				#time.sleep(actuationTime)
			elif(sugarType == Drink.CHOCOLATE):
				print("TODO")
				#ONE OF ABOVE METHODS
			else:
				print("INVALID SUGAR TYPE PASSED TO FUNCTION - TRY SIMPLE_SYRUP CONSTANT")
		else:
			print("INVALID SUGAR LEVEL PASSED TO FUNCTION - TRY VALUE 0 TO 8")

	###
	# Move belt conveyor to position cups under add-on product pumps
	#
	# @direction - Clockwise or Counter Clockwise rotation on main conveyor belt
	# @positions - Number of unit steps to move conveyor belt
	#
	# return NOTHING
	###
	def moveConveyor(direction, positions):
		if(direction == Actuator.FORWARD):
			for i in range(1, positions+1):
				conveyor.run(Actuator.CW) #or Actuator.FORWARD
		elif(direction == Actuator.BACKWARDS):
			for i in range(1, positions+1):
				conveyor.run(Actuator.CCW) #or Actuator.FORWARD
		else:
			print("INVALID CONVEYOR DIRECTION PASSED TO FUNCTION - TRY FORWARD OR BACKWARDS")


if __name__ == "__main__":

	currentNumberOfOrders = 0
	numOfOrdersInProgress = 1
	vendQueue[10] = {}

	# DEFINE ALL ACTUATOR OBJECT
	cupSepServo1Pins = [VCC, BCM8, GND] #cupSeparatorServo1Wires = [VCC, 9, GND]
	cupSeparatorServo1 = Actuator("S", cupSepServo1Pins, "Seamuing MG996R", Actuator.CW)
	cupSepServo2Pins = [VCC, BCM8, GND] #cupSeparatorServo2Wires = [VCC, 9, GND]
	cupSeparatorServo2 = Actuator("S", cupSepServo2Pins, "Seamuing MG996R", Actuator.CCW)

	simpleSyrupSugarPins = [VCC, 4, GND]  	#TODO GPIO4 = BOARD7
	simpleSyrupSugarMotor =  Actuator("R", simpleSyrupSugarPins, "RELAY BOARD", Actuator.CW)
	carmelSugarPins = [VCC, 17, GND]	# GPIO? =
	carmelSugarMotor =  Actuator("R", carmelSugarPins, "RELAY BOARD", Actuator.CW)
	vanillaSugarPins = [VCC, 27, GND]	# GPIO? =
	vanillaSugarMotor = Actuator("R", vanillaSugarPins, "RELAY BOARD", Actuator.CW)
	chocolateSugarPins = [VCC, 22, GND]	# GPIO? =
	chocolateSugarMotor =  Actuator("R", chocolateSugarPins, "RELAY BOARD", Actuator.CW)

	halfHalfMilkPin = [VCC, 18, GND]	# GPIO? =
	halfHalfMilkMotor = Actuator("R", halfHalfMilkPin, "RELAY BOARD")
	almondMilkPin = [VCC, 23, GND]		# GPIO? =
	almondMilkMotor = Actuator("R", almondMilkPin, "RELAY BOARD")
	oatlyMilkPin = [VCC, 24, GND]		# GPIO? =
	oatlyMilkMotor = Actuator("R", oatlyMilkPin, "RELAY BOARD")

	conveyorMotor1Pins = [PWR_12V, GND, VCC_5V, GND, 12, 16]	# GPIO12 =
	conveyorMotor1 = Actuator("M", conveyorMotor1Pins, "Mountain ARK Mini T100 Tank SR-Series")
	conveyorMotor2Pins = [PWR_12V, GND, VCC_5V, GND, 20, 21]	# GPIO20 =
	conveyorMotor2 = Actuator("M", conveyorMotor2Pins, "Mountain ARK Mini T100 Tank SR-Series")

	actuatorObjects = [cupSeparatorServo1, cupSeparatorServo2, simpleSyrupSugarMotor, carmelSugarMotor, vanillaSugarMotor, chocolateSugarMotor, halfHalfMilkMotor]

	while(numOfOrdersInProgress < currentNumberOfOrders):
		vendingDrink = vendQueue[0] # vendingDrink is drink currently in process
		if(vendingDrink.getSugarType != NONE):
			actuateSugarMotor(vendingDrink.getSugarType, vendinfDrink.getSugarLevel)

		if(vendingDrink.getMilkType != NONE):
			actuateMilkMotor(vendingDrink.getMilkType, vendinfDrink.getMilkLevel)

		shiftQueue()
