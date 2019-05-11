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

	#TODO: What variable type should go in default database?
	userDatabase = {
		0: Drink(, 1.1019, 0),
		1: "David",
		2: "Murali"
	}
        lastDrink = NONE
        favoriteDrinks = [NONE, NONE, NONE, NONE, NONE]
	# TODO Define drinkID protocal - Thinking D.CSA9 where:
	# D is drink name (1 = Cold Brew)
	# C is cream level 0 to 8
	# S is sugar level 0 to 8
	# A is boolean latte art request (0 = NO ART, 1 to 8 is 8 different PNGs)
	# 9 is end of line value to search for , so that more Add-Ons can be added to DrinkID protocal
	def __init__(self, firstName, drinkID, userID):
		self.firstName = firstName
		self.userID = userID
		self.drinkObject = Drink(drinkID)
		self.lastDrink = drinkOject.lastDrink
		self.favoriteDrinks = drinkObject.favoriteDrinks #Array holding ??? number of drinks

	###
	# Search user database (python Dictionary) to find user data
	# Jump table / switch statement is much faster than an if-else-if ladder
	# TODO https://jaxenter.com/implement-switch-case-statement-python-138315.html
	# @userIdNum - ID number of user you are searching for
	#
	# @return - String variable with first name (only) of user. (PRIVACY MATTERS!)
	###
	def GetUserFirstName(userIdNum):
		return self.userDatabase.get(userIdNum, " ")


if __name__ == "__main__":
	print("TEST")

