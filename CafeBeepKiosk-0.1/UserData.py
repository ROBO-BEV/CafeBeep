#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-12"
__doc__ =     "Class to locally search user information, with data pulled and pushed from servers (AWS)"

# Useful system jazz
import sys, time, traceback, argparse, string

#BEEP BEEP code that defines valid drink configurtions for each kiosk
import Drink

class UserData:
	MAX_USERS_PER_KIOSK = 4000 # Determine this limit via testing
	AWS = -1
	USB = -2
	AWS_DYNAMO_DB_URL = "https://www.????.com"

	#TODO Can you replace string form Drink() object
	userLocalDatabase = {
		0: "Blaze",
		1: "David",
		2: "Murali"
	}

        ###
        # Constructor to initialize an UserData object, which holds Drink() object
        #
        # @self - Newly created object
        # @firstName -First name of user. Last name not require to protect privacy
	# @userID - Internal BEEP BEEP Technology Inc ID number to ??? upto 32bit users
	# @phoneNUmber - First user phone number to connected to a specific userID

	# phoneNumbers - Array to hold upto 8 phone numbers for a single userID
	# drinkObject - Drink() object that holds drinkName, addOnType, and addOnLevels
	# lastDrink - Last drink ordered from ANY cafeBEEP on Earth
	# favoritrDrinks - Array that holds your five favorite drink configurations
	###
	def __init__(self, firstName, userID, phoneNumber):
		self.firstName = firstName
		self.userID = userID
		self.phoneNumbers[0] = phoneNumber
		self.drinkObject = Drink(Drink.NONE, [Drink.NONE, Drink.NONE, Drink.NONE], [0, 0])
		self.lastDrink = Drink.NONE
		self.favoriteDrinks = [Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE]

	###
	# Search user database (python Dictionary) to find user data
	# Jump table / switch statement is much faster than an if-else-if ladder
	# TODO https://jaxenter.com/implement-switch-case-statement-python-138315.html
	# @userID - ID number of user you are searching for
	#
	# @return - String variable with first name (only) of user. (PRIVACY MATTERS!)
	###
	def getUserFirstName(userID):
		return userLocalDatabase.get(userID, " ").firstName

	###
	# Copy user database (python Dictionary) from non-local source
	# Jump table / switch statement is much faster than an if-else-if ladder
	# TODO https://jaxenter.com/implement-switch-case-statement-python-138315.html
	#
	# @currentLocalUserDatabase - Current Python Dictionary stored in RAM and non-volatile ROM
	# @source - Location (e.g. Amazon AWS) to get most up-to-date database from
	#
	# return NOTHING
	###
	def updateLocalUserDatabase(currentLocalUserDatabase, source):
		# TODO COPY DATA FROM SOURCE INTO / OVER currentLocalUserDatabase

		if(source == AWS):
			print("TODO AWS DYNAMO DB API CALLS")
		elif(source == USB):
			print("TODO READ TEXT FILE FROM USB")
		else:
			print("INVLAID SOURCE FOR USER DATABASE UPDATE: USE AWS OR USB FLASHDRIVE")

if __name__ == "__main__":

	print("START USERDATA.PY MAIN")

	print("END USERDATA.PY MAIN")

