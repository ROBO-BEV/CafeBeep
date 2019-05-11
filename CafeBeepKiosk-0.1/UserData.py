#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-10"
__doc__ =     "Class to locally search user information, with data pulled and pushed from servers (AWS)"

#Useful web IDE to test Flask programs on https://repl.it/

# Useful system jazz
import sys, time, traceback, argparse, string



class UserData:
	MAX_USERS_PER_KIOSK = 4000 # Determine this limit via testing
	AWS = -1
	USB = -2

	#TODO: What variable type should go in default database and how do I update the self.drinkObject?
	userDatabase = {
		0: UserData("Blaze", 0),
		1: "David",
		2: "Murali"
	}

	def __init__(self, firstName, userID):
		self.firstName = firstName
		self.userID = userID
		self.drinkObject = Drink(Drink.NONE, [Drink.NONE, Drink.NONE, Drink.NONE], [0, 0])
		self.lastDrink = Drink.NONE
		self.favoriteDrinks = [Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE]

	###
	# Search user database (python Dictionary) to find user data
	# Jump table / switch statement is much faster than an if-else-if ladder
	# TODO https://jaxenter.com/implement-switch-case-statement-python-138315.html
	# @userIdNum - ID number of user you are searching for
	#
	# @return - String variable with first name (only) of user. (PRIVACY MATTERS!)
	###
	def getUserFirstName(userIdNum):
		return self.userDatabase.get(userIdNum, " ").firstName

	def updateUserDatabase(source):
		if(source == AWS):
		elif(source == USB):
		else:
			print("INVLAID SOURCE FOR USER DATABASE UPDATE: USE AWS OR USB FLASHDRIVE")

if __name__ == "__main__":

	print("END USERDATA MAIN")

