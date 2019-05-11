#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-11"
__doc__ =     "Class to define valid drink configurtions for each kioks"

# Useful system jazz
import sys, time, traceback, argparse, string

DEBUG = True

class Drink:
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
	SOY = -22
	OATLY_XXX = -23

	ART_TYPE = -3
	NO_ART = -31
	BEEP_LOGO = -32
	LEAF = -33
	ROBOT = -34
	N_A = -35

        ##
        # Constructor to initialize an Drink object
        #
        # @self - Newly created object
	# @drinkName - Human readable name of drink (e.g. Cold Brew,  Espresso, etc)
	# @addOnTypes - Array holding product names to be added to a drink
	#		addOnTypes[0] is name of milk being added toi drink
	#		addOnTypes[1] is name of sugar being added to drink
	#		addOnTypes[0] is filename of art being added to drink
	# @addOnLevels - Array holding amount / level of product to be added to a drink
	#
        # return NOTHING
        ##
	def __init__(self, drinkName, addOnTypes, addOnLevels): 	#def __init__(self, drinkID):
		for i in addOnLevels:
			if(addOnLevels[i] > 5):
				debugPrint("ERROR: You created a Drink() object with add-on level greater then 5")
				#TODO EXIT CONSTRUCTOR
			else:
				self.drinkName = drinkName		#getDrinkName(int(drinkID))
				self.addOnTypes = addOnTypes
				self.addOnLevles = addOnLevels

        ###
        # Get product name of sugar in drink
        #
        # @self - Instance of object being called
        #
        # return String variable of product name
        ###
	def getSugarType(addOnTypes):
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
	# return NOTHING
	###
	def debugPrint(stringToPrint):
		if(DEBUG):
			print(stringToPrint)
		else:
			print("/n") # PRINT NEW LINE

if __name__ == "__main":
	addOnTypes = [NONE, HALF_HALF, "NO_ART.png"]
	addOnLevels = [NONE, 3, N_A]
	drinkForBlaze = Drink(COLD_BREW, addOnTypes, addOnLevels)
	#drinkID = 1.0109039
	#drinkForDavid = Drink(drinkID)

	print("END MAIN IN DRINK CLASS")
