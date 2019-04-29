#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-04-23"
__doc__ =     "Class to store and search user information"

#Useful web IDE to test Flask programs on https://repl.it/

# Useful system jazz
import sys, time, traceback, argparse, string


class UserData:
	MAX_USERS_PER_KIOSK = 4000 # Determine this limit via testing

	userDatabase = {
		0: "Blaze",
		1: "David"
	}

	def __init__(self, firstName, drinkName, userID):
		self.firstName = firstName
		self.drinkName = drinkName
		self.userID = userID

	###
	# Search user database (python Dictionary) to find user data
	# Jump table / switch statement is much faster than an if-else-if ladder
	# TODO https://jaxenter.com/implement-switch-case-statement-python-138315.html
	# @userIdNum - ID number of user you are searching for
	#
	# @return - String variable with first name (only) of user. (PRIVACY MATTERS!)
	###
	def GetUserFirstName(userIdNum):
		userDatabase = {
			0: "Blaze",
			1: "David",
			15105139110: "Blaze's CellPhone"
		}
		return userDatabase.get(userIdNum, " ")


	if __name__ == "__main__":
		print("TEST")

