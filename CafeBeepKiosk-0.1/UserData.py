#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-25"
__doc__ =     "Class to locally search user information, with data pulled and pushed from servers (AWS)"

# Useful system jazz
import sys, time, traceback, argparse, string

# Read Comma Separated Value (CSV) files from external storage
# FIND LINK
import csv

# Double-ended queue which is implemented as a doubly-linked list interally
# https://docs.python.org/2/library/collections.html
import collections

# Provide C compatible data types (e.g. unsigned integers) and allows calling functions in DLLs
# https://docs.python.org/2/library/ctypes.html
import ctypes

# BEEP BEEP code that defines valid drink configurtions for each kiosk
import Drink


class UserData:

	DEBUG_STATEMENTS_ON = True
	FILEPATH_ERROR = -1
	OK = 0

	MAX_USERS_PER_KIOSK = 4000 # Determine this limit via testing
	AWS = -1
	USB_FLASHDRIVE = -2
	PI_SD_CARD = -3
	AWS_DYNAMO_DB_URL = "https://www.????.com"

	nextUserIDtoAssign = c_uint(0) # Ctype Unsigned Integer to give max number of userID's

        ###
        # Constructor to initialize an UserData object, which holds Drink() object
        #
        # @self - Newly created object
        # @firstName -First name of user. Last name not require to protect privacy
	# @userID - Internal BEEP BEEP Technology Inc ID number up to 4,294,967,295 (32-bit unsigned interger)
	# @phoneNUmber - First user phone number to connected to a specific userID

	# phoneNumbers - Array to hold upto 8 phone numbers for a single userID
	# drinkObject - Drink() object that holds currently selected drinkName, addOnType, and addOnLevels
	# lastDrink - Last drink ordered from ANY cafeBEEP kiosk in the Sol Star System
	# freqDrinks - An auto currated list of the three most ordered drinks by a user
	# TODOv2019.0 favoriteDrinks - Array that holds five drink configurations manually favorited by user
	# fullOrderHistoy - Doubly-linked list of an users entire order history from ANY cafeBEEP kiosk
	###
	def __init__(self, firstName, userID, phoneNumber):
		self.firstName = firstName
		self.userID = nextUserIDtoAssign
		nextUserIDtoAssign += 1
		self.phoneNumnbers = [0, 0, 0, 0, 0, 0, 0, 0]
		self.phoneNumbers[0] = phoneNumber
		self.drinkObject = Drink(Drink.NONE, [Drink.NONE, Drink.NONE, Drink.NONE], [0, 0])
		self.lastDrinks = [Drink.NONE, Drink.NONE, Drink.NONE]
		self.freqDrinks = [Drink.NONE, Drink.NONE, Drink.NONE]
		#TODOv2019.0 self.favoriteDrinks = [Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE]
		self.fullOrderHistory = collections.deque()

	###
	# Add newly ordered drink to the HEAD (beginning) of the full order history, and determine
	# what the three most ordered and last three drinks of a single user are.
	#
	# @self - Instance of UserData object being called
	# @newDrink - Drink configuration to add to user order history
	#
	# return NOTHING
	###
	def updateDrinkHistory(self, newDrink):
		# Add drink to front of the doubly-linked list
		self.fullOrderHistory.appendleft(newDrink) #TODO Are Linked Lists zero indexed

		# Update lastDrinks array via function input parmeter and doubly-linked list
		#self.lastDrinks[2] = self.fullOrderHistory(2)
		#self.lastDrinks[1] = self.fullOrderHistory(1) TODO Are Linked Lists zero indexed
		#self.lastDrinks[0] = newDrink

		#TODO DETERMINE IF THIS IS FASTER THEN LINKED LIST METHOD ABOVE
		# Add drink to index zero of lastDrinks array and shift older drink order one position
		self.lastDrinks[2] = self.lastDrinks[1]
		self.lastDrinks[1] = self.lastDrinks[0]
		self.lastDrinks[0] = newDrink

		self.updateDrinkFavorites()

	###
	# Transverse full order history and determine what three most ordered drinks are
	# TODO Uses algothrim from Stack Overflow "How to count frequency of the elements in a list" 
	# @self - Instance of UserData object being called
	#
	# return NOTHING
	###
	def updateDrinkFavorites(self):
		#TODOv2019.0 self.favoriteDrinks = [Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE]

		# https://docs.python.org/2/library/collections.html
		#TODO self.fullOrderHistory.count(1.214121)

		freqCount = collections.Counter(self.fullOrderHistory)
		collectionTuple = freqCount.most_common(3)
		debugPrint(collectionTuple) #TODO [(object1, FREQ1), (object2, FREQ2), (object3, FREQ3)]
		freqDrinks[0] = collectionTuple(0, 1)
		freqDrinks[1] = collectionTuple(1, 1)
		freqDrinks[2] = collectionTuple(2, 1)


		self.freqDrinks[0] = self.fullOrderHistory(0) #TODO Is LL zero indexed???
		for nodeNum in self.fullOrderHistory:
			if(self.freqDrinks[0] == self.fullOrderHistory(nodeNum+1)):
				print("DO NOTHING")
			else:
				self.freqDrinks[1] = self.fullOrderHistory(nodeNum+1)

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



	def updateNonLocalDatabase():
		print("#PUSH nextUserIDtoAssign to cloud")


	###
	# Import user database to python Dictionary from non-local source
	# Jump table / switch statement is much faster than an if-else-if ladder
	# TODO https://jaxenter.com/implement-switch-case-statement-python-138315.html
	#
	# @currentLocalUserDatabase - Current Python Dictionary stored in RAM and non-volatile ROM
	# @source - Location (e.g. Amazon AWS) to get new database from
	#
	# return NOTHING
	###
	def updateLocalUserDatabase(currentLocalUserDatabase, source):
		# TODO COPY DATA FROM SOURCE INTO / OVER currentLocalUserDatabase

		#TODO Can you replace string form Drink() object
		# Use phone numebr as key and then search for active phone numbers
		userLocalDatabase = {
			15105139110: UserData("Blaze", 0, 15135109110)
		}


		if(source == AWS):
			print("TODOv2019.0 AWS DYNAMO DB API CALLS")
		elif(source == USB_FLASHDRIVE):
			errorCode = writeCSV('E:/')
		elif(source == PI_SD_CARD):
			errorCode = writeCSV('TODO')
		else:
			print("INVLAID SOURCE FOR USER DATABASE UPDATE: USE AWS, PI SD CARD, OR USB FLASHDRIVE")

		return errorCode

	###
	# Read Comma Separated Value (CSV) data into locally connect storage (SD card, Flashdrive, or TODO)
	# NOTE: Code doesn't current work on Windows with their dumb ass backward slash :)
	#
	# @filepath - Full filepath to write CSV file to. Must including the final forward slash '/'
	#
	# return FILEPATH_ERROR code if invalid filepath passed as parameter, OK otherwise
	###
	def readCSV(filepath):
		if(not filepath.endswith('/)')
			debugPrint("HEY DUMB ASS END YOUR FILEPATH WITH A '/' CHARACTER!!!")			
			return FILEPATH_ERROR

		debugPrint("START READING CSV FILE FROM " + filepath + "UserDataDatabase1.csv")
		with open(filepath + '/UserDataDatabase1.csv', newline = '') as csvfile:
			userDataReader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
			lineCount = 0
		for row in userDataReader:
			for i in range(2, 10):	# 2 to 9
				tempPhoneNumbers[i] = row[i]
			for j in range(10, 14): # 11 to 13
				tempAddOnTypes[j] = row[j]
			for k in range(14, 16): # 14 to 15
				tempAddOnLevels[k] = row[k]

		tempUser = UserData(row[0], row[1], tempPhoneNumbers)
		tempDrink = Drink(row[10], tempAddOnTypes, tempAddOnLevels)
		tempUser.setDrink(tempDrink)
		tempUser.setLastDrink(row[16])
		tempUser.setFavoriteDrinks(row[17], row[18], row[19], row[20], row[21])

		#print(', '.join(row))

		for userID in range(0, MAX_USERS_PER_KIOSK+1):
			setDictionary(userID)

		debugPrint("END READING TEXT FILE FROM " + filepath)

		return OK

	###
	# Calls standard Python 3 print("X") statement if DEBUG global variable is TRUE
	#
	# return String variable passed as input parameter
	###
	def debugPrint(stringToPrint):
		if(DEBUG_STATEMENTS_ON):
			print("UserData.py DEBUG STATEMENT: " + stringToPrint)
		else:
			print("/n") # PRINT NEW LINE / DO NOTHING

if __name__ == "__main__":

	print("START USERDATA.PY MAIN")

	print("END USERDATA.PY MAIN")

