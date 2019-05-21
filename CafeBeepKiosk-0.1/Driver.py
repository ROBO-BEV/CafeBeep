#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-18"
__doc__ =     "Logic to run cafeBEEP kiosk back-end"

# Useful system jazz
import sys, time, traceback, argparse, string

# Allow UDP communication between different CPUs (e.g. Raspberry Pi, NVIVDIA TX2, etc) using Ethernet
import socket

GUI_PI_IP = "127.168.1.69"
VEND_PI_IP = "127.168.1.135"
GUI_TX2_IP = "127.168.1.42"

UDP_PORT = 5005

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

MAX_VEND_QUEUE_SIZE = 10	# cafeBEEP v2019.0 kiosk can process upto 10 drinks at a drink
MAX_ADDON_DISPENSE_TIME = 2	# 2 Seconds is the max time sugar, milk, and powder takes to dispense


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
# @actuatorObjects - Array of Servo() objects to control
#
# return NOTHING
###
def dropCup(actuatorObjects):
	for i in actuatorObjects:			# Move ALL actuators to drop cup to min position at the same time
		actuatorObjects[i].min()		# OLD WAY cupSeparatorServo1.min()
							#actuatorObjects[1].min()
	time.sleep(1.500) 				# TODO REAL LIFE TESTING Pause 1500 ms
	for j in actuatorObjects:			# Move ALL actuators to drop cup to max position at the same time
		actuatorObjects[j].max()		# OLD WAY cupSeparatorServo1.min()
							#actuatorObjects[1].max()

###
# Actuate linear actuators to push cup into onf of the user vend ports
# NOTE: HARD CODED LINEAR ACTUATOR OBJECT
#
# @actuatorObjects - Array of Relay() / linear actuator objects to control
#
# return NOTHING
###
def liftCup(actuatorObjects):
	for i in actuatorObjects:  		# Move ALL actuators to drop cup to min position at the same time
		actuatorObjects[i].min()

	time.sleep(1.700) 			# TODO REAL LIFE TESTING Pause 1700 ms
	for i in actuatorObjects:		# Move ALL actuators to drop cup to max position at the same time
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
# NOTE: SUGAR TYPE IS HARD CODED TO ACTUATOROBJECTS ARRAY AND MUST MATCH __MAIN__ CONFIGURATION
#
# @actuatorObjects - Array of Actuator.py objects
# @sugarType - Product name of sugar add-on to dispense (e.g. SIMPLE_SYRUP)
# @sugarLevel - Amount of sugar units to dispense 1 = ?? oz
#
# return NOTHING
###
def actuateSugarMotor(actuatorObjects, sugarType, sugarLevel):
	if(Drink.NONE <= sugareLevel and sugarLevel < Drink.MAX_SUGAR_LEVEL):
		actuationTime = sugarLevel / Drink.SUGAR_FLOW_RATE  #Units of Seconds based on flow rate per second of pump
		if(sugarType == NONE):
			time.sleep(0.001) # DO NOTHING expect pause for 1 millisecond
		elif(sugarType == Drink.SIMPLE_SYRUP):
			print("TODO")
			actuatorObjects[0].run(actuationTime, Actuator.N_A, 0.5, Actuator.FORWARD) #PROBABLY CORRECT
			#simpleSyrupSugarMotor.run(actuationTime, Actuator.N_A, 0.5, Actuator.FORWARD) #PROBABLY WRONG
		elif(sugarType == Drink.CARMEL):
			print("TODO")
			#actuatorObjects[1].
			self.run(actuationTime, Actuator.N_A, 0.5, Actuator.FORWARD) #PROBABLY WRONG
		elif(sugarType == Drink.Vanilla):
			print("TODO")
			#actuatorObjects[2].
			#time.sleep(actuationTime)
		elif(sugarType == Drink.CHOCOLATE):
			print("TODO")
			#actuatorObjects[1].
			#ONE OF ABOVE METHODS
		else:
			print("INVALID SUGAR TYPE PASSED TO FUNCTION - TRY SIMPLE_SYRUP CONSTANT")
	else:
		print("INVALID SUGAR LEVEL PASSED TO FUNCTION - TRY VALUE 0 TO 8")

###
# Move belt conveyor to position cups under add-on product pumps
#
# @direction - Clockwise or Counter Clockwise rotation on main conveyor belt
# @numOfPositions - Number of unit steps to move conveyor belt
#
# return NOTHING
###
def moveConveyor(actuatorObjects, direction, numOfPositions):
	if(direction == Actuator.FORWARD):
		for posNum in range(1, numOfPositions+1):
			for i in actuatorObjects: 			# Move ALL actuators to drop cup to min position at the same time
				actuatorObjects[i].run(Actuator.CW) 	#or Actuator.FORWARD
			time.sleep(MAX_ADDON_DISPENSE_TIME)		#Units are Seconds
	elif(direction == Actuator.BACKWARDS):
		for posNum in range(1, numOfPositions+1):
			for i in actuatorObjects: 			# Move ALL actuators to drop cup to min position at the same time
				actuatorObjects[i].run(Actuator.CCW) 	#or Actuator.BACKWARD
			time.sleep(MAX_ADDON_DISPENSE_TIME)		#Units are Seconds
	else:
		print("INVALID CONVEYOR DIRECTION PASSED TO FUNCTION - TRY FORWARD OR BACKWARDS")

###
# Pull data from separate CPU running menu selection GUI
#
# @bufferSize - UDP buffer for collect ALL GUI orders
###
def getOrder(bufferSize):
	rxSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	rxSockey.bind((VEND_PI_IP, UDP_PORT)) #or GUI_PI_IP???
	data, addr = rxSocket.recvfrom(bufferSize)
	return data

if __name__ == "__main__":

	currentNumberOfOrders = 0
	numOfOrdersInProgress = 1

	tempDrink = Drink(Drink.NONE, Drink.NONE, Drink.NONE)
	vendQueue[MAX_VEND_QUEUE_SIZE] =  [tempDrink, tempDrink, tempDrink, tempDrink, tempDrink, tempDrink, tempDrink, tempDrink, tempDrink, tempDrink]

	# DEFINE ALL ACTUATORS INSIDE CAFEBEEP KIOSK ATTACH TO ADAFRUIT DC & STEPPER MOTOR HAT 2348
	cupSepServo1Pins = [VCC_5V, GND, 5]  		# GPIO5 = BOARD29 = DC_STEPPER_HAT???
	cupSeparatorServo1 = Actuator("S", cupSepServo1Pins, "Seamuing MG996R", Actuator.CW)
	cupSepServo2Pins = [VCC_5V, GND, 6]  		# GPIO6 = BOARD31 = DC_STEPPER_HAT???
	cupSeparatorServo2 = Actuator("S", cupSepServo2Pins, "Seamuing MG996R", Actuator.CCW)

	simpleSyrupSugarPins = [PWR_12V, GND, 4]	#TODO GPIO4 = BOARD7 = DC_STEPPER_HAT???
	simpleSyrupSugarMotor =  Actuator("R", simpleSyrupSugarPins, "Zjchao 202", Actuator.CW)
	carmelSugarPins = [PWR_12V, GND, 17]		#TODO GPIO17 = BOARD11 = DC_STEPPER_HAT???
	carmelSugarMotor =  Actuator("R", carmelSugarPins, "Zjchao 202", Actuator.CW)
	vanillaSugarPins = [PWR_12V, GND, 27]		#TODO GPIO27 = BOARD? = DC_STEPPER_HAT???
	vanillaSugarMotor = Actuator("R", vanillaSugarPins, "Zjchao 202", Actuator.CW)
	chocolateSugarPins = [PWR_12V, GND, 22]		#TODO GPIO22 =
	chocolateSugarMotor =  Actuator("R", chocolateSugarPins, "Zjchao 202", Actuator.CW)

	halfHalfMilkPin = [PWR_12V, GND, 18]		#TODO GPIO18 =
	halfHalfMilkMotor = Actuator("R", halfHalfMilkPin, "Zjchao 202", Actator.CW)
	almondMilkPin = [PWR_12V, GND, 23]		#TODO GPIO23 =
	almondMilkMotor = Actuator("R", almondMilkPin, "Zjchao 202", Actator.CW)
	oatlyMilkPin = [PWR_12V, GND, 24]		#TODO GPIO24 =
	oatlyMilkMotor = Actuator("R", oatlyMilkPin, "Zjchao 202", Actator.CW)

	#TODO GPIO12 = BOARD? = DC_STEPPER_HAT???   / GPIO16 = BOARD? = DC_STEPPER_HAT???
	conveyorMotor1Pins = [PWR_12V, GND, VCC_5V, GND, NO_PIN, NO_PIN, 12, 16]
	conveyorMotor1 = Actuator("M", conveyorMotor1Pins, "Mountain ARK Mini T100 Tank SR-Series")
	conveyorMotor2Pins = [PWR_12V, GND, VCC_5V, GND, NO_PIN, NO_PIN, 12, 16]
	conveyorMotor2 = Actuator("M", conveyorMotor2Pins, "Mountain ARK Mini T100 Tank SR-Series")

	#TODO GPIO20 = BOARD? = DC_STEPPER_HAT?   / GPIO21 = BOARD? = DC_STEPPER_HAT?
	liftMotor1pins = [PWR_12V, GND, 20, 21]
	liftMotor1 = Actuator("M", liftMotor1pins, "??? Linear Actuator")
	liftMotor2pins = [PWR_12V, GND, 20, 21]
	liftMotor2 = Actuator("M", liftMotor2pins,  "??? Linear Actuator")

	# SEPARATE FULL LIST OF ACTUATOR OBJECTS INTO MORE SPECIFIC ARRAY GROUPINGS
	actuatorObjects = [cupSeparatorServo1, cupSeparatorServo2, simpleSyrupSugarMotor, carmelSugarMotor, vanillaSugarMotor, chocolateSugarMotor, halfHalfMilkMotor, almondMilkMotor, oatlyMilkMotor, conveyorMotor1, conveyorMotor2]
	dropCupActuators = [actuatorObjects[0], actuatorObjects[1]]
	sugarActuators = [actuatorObjects[2], actuatorObjects[3], actuatorObjects[4], actuatorObjects[5]]
	milkActuators = [actuatorObjects[6], actuatorObjects[7], actuatorObjects[8]]
	conveyorActuators = [actuatorObects[9], actuatorObjects[10]]

	while(True):
		for drinkNum in range(0, MAX_VEND_QUEUE_SIZE-1):
			vendQueue[drinkNum] = getOrder(UDP_FOR_OTHER_PI)
			if(vendQueue[drinkNum] != Drink.NONE):
				dropCup(dropCupActuators)
				moveConveyor(conveyorActuators, Actuator.FORWARD, 1)
				actuateSugarMotor(sugarActuators, vendQueue[drinkNum].getSugarType, vendQueue[drinkNum].getSugarLevel)

				vendQueue[drinkNum+1] = getOrder(UDP_FOR_OTHER_PI)
				dropCup(dropCupActuators)
				moveConveyor(conveyorActuators, Actuator.FORWARD, 1)
				actuateMilkMotor(milkActuators, vendQueue[drinkNum].getSugarType, vendQueue[drinkNum].getSugarLevel)
				actuateSugarMotor(sugarActuators, vendQueue[drinkNum+1].getSugarType, vendQueue[drinkNum+1].getSugarLevel)

				#DO POWDER ADD_ON NEXT

				#MOVE TO LIFT VEND PORT
				liftCup()


	while(numOfOrdersInProgress < currentNumberOfOrders):
		vendingDrink = vendQueue[0] # vendingDrink is drink currently in process
		if(vendingDrink.getSugarType != NONE):
			actuateSugarMotor(vendingDrink.getSugarType, vendingDrink.getSugarLevel)

		if(vendingDrink.getMilkType != NONE):
			actuateMilkMotor(vendingDrink.getMilkType, vendingDrink.getMilkLevel)

		shiftQueue()
