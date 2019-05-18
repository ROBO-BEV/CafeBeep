#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-17"
__doc__ =     "Class to define valid drink configurtions for each kioks"

# Useful system jazz
import sys, time, traceback, argparse, string

class Drink:
	DEBUG_STATEMENTS_ON = True

	# Drink Name Constants
	COLD_BREW = 0
	HEATED_COLD_BREW = 1
	HOT_DRIP_COFFEE = 2
	ESPRESSO = 3
	LATTE = 4
	MOCHA = 5
	HOT_CHOCOLATE = 6

	# AddOn Type Constants
	NONE = 0

	SUGAR_TYPE = -1
	SIMPLE_SYRUP = -11
	CARMEL = -12
	VANILLA = -13
	CHOCOLATE = -14
	MAX_SUGAR_LEVEL = 8 	# 0 to 8 sugar "packets"
	SUGAR_FLOW_RATE = 10 # Units of sugar level / sec = oz / sugar level / sec

	MILK_TYPE = -2
	HALF_HALF = -21
	SOY_MILF = -22
	OATLY_MILF = -23
	MAX_MILK_LEVEL = 8 	# 0 to 8 0.25 oz of milk shots
	MILK_FLOW_RATE = 10 # Units of sugar level / sec = oz / sugar level / sec

	ART_TYPE = -3
	NO_ART = -31
	BEEP_LOGO = -32
	LEAF = -33
	ROBOT = -34

	# Lid Color Constants
	BLACK = -4
	WHITE = -5
	RED = -6
	ORANGE = -7
	PINK = -8
	GREEN = -9
	BLUE = -10
	PURPLE = -11

        ##
        # Constructor to initialize an Drink object
        #
        # @self - Newly created object
	# @drinkName - CONSTANT product name of drink (e.g. COLD_BREW, ESPRESSO, etc)
	# @addOnTypes - Array holding product names to be added to a drink
	#		addOnTypes[0] is CONSTANT product name of milk being added to drink
	#		addOnTypes[1] is CONSTANT product name of sugar being added to drink
	#		addOnTypes[2] is .png filename of art being added on top of drink
	# @addOnLevels - Array holding amount / level of product to be added to a drink
	#
	# lidColor - For v2019.0 lid color defaults to black
	#	     v2019.1 web app with allow user to select personalized color
	# size - For v2019.0 size defaults to 10 ounces
	#            v2019.1 and later may default larger or smaller, depending on user feedback
        # return NOTHING
        ##
	def __init__(self, drinkName, addOnTypes, addOnLevels):
		for i in range(0, len(addOnLevels)-1):
			print(i)
			if(addOnLevels[i] > 5):
				debugPrint("ERROR: You created a Drink() object with add-on level greater then 5")
				__exit__() #TODO EXIT CONSTRUCTOR
			else:
				self.drinkName = drinkName
				self.addOnTypes = addOnTypes
				self.addOnLevles = addOnLevels

		self.lidColor = Drink.BLACK 	# Default to black in constructor and update via web app
		self.size = 10		# Units are ounces

	###
	#
	#
        # @self - Instance of object being called
	#
	# return object that created exception
	####

	def __enter__(self):
		print("in __enter__")
		return self

	###
	#
	#
        # @self - Instance of object being called
	#
	#
	#
	####
	def __exit__(self, exception_type, exception_value, traceback):
		print("in __exit__")


        ###
        # Get product name of sugar in drink
        #
        # @self - Instance of object being called
        #
        # return String variable of product name
        ###
	def getSugarType(self):
		return self.addOnTypes[0]

        ###
        # Get product name of milk in drink
        #
        # @self - Instance of object being called
        #
        # return String variable of product name
        ###
	def getMilkType(self, addOnTypes):
		return self.addOnTypes[1]

        ###
        # Get filename for latte art on top of drink
        #
        # @self - Instance of object being called
        #
        # return String variable of filename
        ###
	def getLatteArtType(self, addOnTypes):
		return self.addOnTypes[2]

        ###
        # Get amount / level of sugar in drink
        #
        # @self - Instance of object being called
        #
        # return Integer variable of product level
        ###
	def getSugarLevel(self, addOnTypes):
		return self.addOnLevel[0]

        ###
        # Get amount / level of milk in drink
        #
        # @self - Instance of object being called
        #
        # return Integer variable of product level
        ###
	def getMilkLevel(self, addOnTypes):
		return self.addOnTypes[1]

        ###
        # Set color of drink lid
        #
        # @color - New lid color selected by user (Conctrutor defaults lid to black)
	#
	# self - Instance of object being called
        #
        # return NOTHING
        ###
	def setLidColor(self, color):
		self.lidColor = color


        ###
        # Get current color of drink lid
        #
	# self - Instance of object being called
        #
        # return Lid color constant (e.g. BLACK, PINK, BLUE, etc)
        ###
	def getLidColor(self):
		return self.lidColor

        ###
        # Get current size of drink
        #
	# self - Instance of object being called
        #
        # return Drink size in ounces
        ###
	def getSize(self):
		return self.size


	def createDrinkID(self):
		print("TODO")

        # TODO Define drinkID protocal - Thinking D.CSA9 where:
        # D is drink name (1 = Cold Brew)
        # C is cream level 0 to 5
        # S is sugar level 0 to 5
        # A is boolean latte art request (0 = NO ART, 1 to 8 is 8 different PNGs)
        # 9 is end of line value to search for , so that more Add-Ons can be added to DrinkID protocal
	def decodeDrinkID(self, addOnInfoRequested, drinkID):
		if(addOnInfoRequested == SUGAR_TYPE):
			return #TODO SUBSTRING FIRST DECIMAL POINT
		elif(addOnInfoRequested == MILK_TYPE):
			return #TODO SUBSTRING SECOND DECIMAL POINT
		elif(addOnInfoRequested == ART_TYPE):
			return #TODO SUBSTRING THIRD DECIMAL POINT
		if(addOnInfoRequested == SUGAR_LEVEL):
			return #TODO SUBSTRING FIFTH DECIMAL POINT
		elif(addOnInfoRequested == MILK_LEVEL):
			return #TODO SUBSTRING SIXTH DECIMAL POINT
		else:
			print("INVALID ADD-ON INFO REQUESTED: USE SUGAR, MILK, OR ART TYPE")
	###
	# Calls standard Python 3 print("X") statement if DEBUG global variable is TRUE
	#
	# return String variable passed as input parameter
	###
	def debugPrint(stringToPrint):
		if(DEBUG_STATEMENTS_ON):
			print("Drink.py DEBUG STATEMENT: " + stringToPrint)
		else:
			print("/n") # PRINT NEW LINE / DO NOTHING

if __name__ == "__main__":

	print("START MAIN IN DRINK CLASS")

	addOnTypes = [Drink.NONE, Drink.HALF_HALF, Drink.NO_ART]
	addOnLevels = [Drink.NONE, 3]
	drinkForBlaze = Drink(Drink.COLD_BREW, addOnTypes, addOnLevels)
	drinkForBlaze.setLidColor(Drink.RED)
	print(str(drinkForBlaze.getSize()) + " oz drink coming right up!")

	#drinkForBlaze.getSugarType()
	#drinkID = 1.0109039
	#drinkForDavid = Drink(drinkID)

	print("END MAIN IN DRINK CLASS")
