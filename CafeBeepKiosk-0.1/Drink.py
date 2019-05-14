#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-12"
__doc__ =     "Class to define valid drink configurtions for each kioks"

# Useful system jazz
import sys, time, traceback, argparse, string

class Drink:
	DEBUG = True

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
	CHOCOLATE = -13

	MILK_TYPE = -2
	HALF_HALF = -21
	SOY_MILF = -22
	OATLY_MILF = -23

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
		for i in addOnLevels:
			if(addOnLevels[i] > 5):
				debugPrint("ERROR: You created a Drink() object with add-on level greater then 5")
				__exit__() #TODO EXIT CONSTRUCTOR
			else:
				self.drinkName = drinkName
				self.addOnTypes = addOnTypes
				self.addOnLevles = addOnLevels

		self.lidColor = BLACK 	# Default to black in constructor and update via web app
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
	def getSugarType():
		return self.addOnTypes[0]

        ###
        # Get product name of milk in drink
        #
        # @self - Instance of object being called
        #
        # return String variable of product name
        ###
	def getMilkType(addOnTypes):
		return self.addOnTypes[1]

        ###
        # Get filename for latte art on top of drink
        #
        # @self - Instance of object being called
        #
        # return String variable of filename
        ###
	def getLatteArtType(addOnTypes):
		return self.addOnTypes[2]

        ###
        # Get amount / level of sugar in drink
        #
        # @self - Instance of object being called
        #
        # return Integer variable of product level
        ###
	def getSugarLevel(addOnTypes):
		return self.addOnLevel[0]

        ###
        # Get amount / level of milk in drink
        #
        # @self - Instance of object being called
        #
        # return Integer variable of product level
        ###
	def getMilkLevel(addOnTypes):
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
	def setLidColor(color):
		self.lidColor = color


        ###
        # Get current color of drink lid
        #
	# self - Instance of object being called
        #
        # return Lid color constant (e.g. BLACK, PINK, BLUE, etc)
        ###
	def getLidColor():
		return self.lidColor

        ###
        # Get current size of drink
        #
	# self - Instance of object being called
        #
        # return Drink size in ounces
        ###
	def getSize():
		return self.size


	def createDrinkID():
		print("TODO")

        # TODO Define drinkID protocal - Thinking D.CSA9 where:
        # D is drink name (1 = Cold Brew)
        # C is cream level 0 to 5
        # S is sugar level 0 to 5
        # A is boolean latte art request (0 = NO ART, 1 to 8 is 8 different PNGs)
        # 9 is end of line value to search for , so that more Add-Ons can be added to DrinkID protocal
	def decodeDrinkID(addOnInfoRequested, drinkID):
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
		if(DEBUG):
			print("Drink.py DEBUG STATEMENT: " + stringToPrint)
		else:
			print("/n") # PRINT NEW LINE / DO NOTHING

if __name__ == "__main":
	print("START MAIN IN DRINK CLASS")

	addOnTypes = [NONE, HALF_HALF, NO_ART]
	addOnLevels = [NONE, 3]
	drinkForBlaze = Drink(COLD_BREW, addOnTypes, addOnLevels)
	drinkForBlaze.setLidColor(RED)
	print(drinkForBlaze.getSize() + " oz drink coming right up!")

	#drinkForBlaze.getSugarType()
	#drinkID = 1.0109039
	#drinkForDavid = Drink(drinkID)

	print("END MAIN IN DRINK CLASS")
