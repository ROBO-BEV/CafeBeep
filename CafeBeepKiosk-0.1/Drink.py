
#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-10"
__doc__ =     "Class to define valid drink configurtions for each kioks"

# Useful system jazz
import sys, time, traceback, argparse, string

COLD_BREW = 1
HEATED_COLD_BREW = 2
HOT_DRIP_COFFEE = 3

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
BEEP_LOGO -32
LEAF = -33
ROBOT = -34
N_A = -35

class Drink:

	def __init__(self, drinkID, addOnTypes, addOnLevels):
	def __init__(self, drinkID):
		self.drinkName = getDrinkName(drinkID) 	#int(drinkID)
		self.AddOnTypes = addOnTypes
		self.AddOnLevles = addOnLevels

	def getDrinkName(drinkID):
		return TODO SearchDrinkDatabase

	def getSugarType(addOnTypes):
		return self.addOnTypes[0]

	def getMilkType(addOnTypes):
		return self.addOnTypes[1]

	def getLatteArtType(addOnTypes):
		return self.addOnTypes[2]



	def getSugarLevel(addOnTypes):
		return self.addOnLevel[0]

	def getMilkLevel(addOnTypes):
		return self.addOnTypes[1]


	def createDrinkID():

	def decodeDrinkID(addOnInfoRequested, drinkID)
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

if __name__ = "__main":
	addOnTypes = [NONE, HALF_HALF, "NO_ART.png"]
	addOnLevels = [NONE, 3, N_A]
	drinkForBlaze = Drink(COLD_BREW,addOnTypes, addOnLevels )
	#drinkID = 1.0109039
	#drinkForDavid = Drink(drinkID)

	print("END MAIN IN DRINK CLASS")
