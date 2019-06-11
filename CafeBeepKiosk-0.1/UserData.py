#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-31"
__doc__ =     "Class to locally search user information, with ability to pull and push data from servers and flashdrives"

# Useful system jazz to do the following:
# Interpreter functions, pause program execution, trace runtime errors,
# accept terminal input parameters, and use String variable
import sys, time, traceback, argparse, string

# Read Comma Separated Value (CSV) files from external storage
# https://docs.python.org/3/library/csv.html
import csv

# Double-ended queue which is implemented as a doubly-linked list internally (zero indexed)
# https://docs.python.org/3/library/collections.html
import collections

# Provide C compatible data types (e.g. unsigned integers) and allows calling functions in DLLs
# https://docs.python.org/3/library/ctypes.html
import ctypes

# BEEP BEEP code that defines valid drink configurtions for each kiosk
import Drink

class UserData:

	DEBUG_STATEMENTS_ON = True

	# Useful function return error codes
	OK = 0
	FILEPATH_ERROR = -1
	DATA_CONNECTION_ERROR = -2
	BAD_USER_INPUT_ERROR = -3
	INVALID_USER_ERROR = -4

	MAX_USERS_PER_KIOSK = 4000 		# TODO Determine this limit via testing
	PHONE_NUMBER = "15558675309"			# Constant for fixing user input, which is ALWAYS bad
	FIRST_NAME = "Jane"
	AWS_DATABASE_SERIVCE = "DynamodB"	# Name of AWS database service in use
	USB_FLASHDRIVE = "64GB"			# Max USB flahsdrive size supported is 64 GigaBytes
	PI_SD_CARD = "32GB"			# Max microSD card size supported in 32 GigaBytes
	ONLINE_AWS_DYNAMO_DB_URL = "arn:aws:dynamodb:us-west-1:076571243942:table/UserData"
	DYNAMO_TABLE_NAME = "UserData"		# TODO Database service MUST be named as class they are in

	# Allow users to select font for kiosk display (Customize all the things!)
	SOURCE_SANS_PRO = "Source Sans Pro"
	ARIAL = "Arial"
	COURIER_NEW = "Courier New"

	# Global class variable that is stored locally and on AWS
	nextUserIDtoAssign = 0 #TODO c_unit(0) Ctype Unsigned Integer to give max number of userID's

        ###
        # Constructor to initialize an UserData object, which holds Drink() object
        #
        # @self - Newly created object
        # @firstName -First name of user. Last name not require to protect privacy
	# @userID - Internal BEEP BEEP Technology Inc ID number up to 4,294,967,295 (32-bit unsigned interger)
	# @phoneNUmber - First user phone number to connected to a specific userID

	# phoneNumbers - Array to hold upto 8 phone numbers for a single userID
	# mainPhoneNUmber - Cell phone number that definds public facing userID (TODO different then userID ???)	# drinkObject - Drink() object that holds currently selected drinkName, addOnType, and addOnLevels
	# lastDrink - Last drink ordered from ANY cafeBEEP kiosk in the Sol Star System
	# freqDrinks - An auto currated list of the three most ordered drinks by a user
	# TODOv2019.0 favoriteDrinks - Array that holds five drink configurations manually favorited by user
	# fullOrderHistoy - Doubly-linked list of an users entire order history from ANY cafeBEEP kiosk
	###
	def __init__(self, firstName, userID, phoneNumber):
		self.firstName = firstName
		self.userID = nextUserIDtoAssign
		nextUserIDtoAssign += 1
		self.phoneNumbers = [0, 0, 0, 0, 0, 0, 0, 0]
		self.mainPhoneNumber = phoneNumbers[0] = sanitizeUserInput(phoneNumber, PHONE_NUMBER)
		self.drinkObject = Drink(Drink.NONE, [Drink.NONE, Drink.NONE, Drink.NONE], [0, 0])
		self.preferredFont = SOURCE_SANS_PRO
		self.lastDrinks = [Drink.NONE, Drink.NONE, Drink.NONE]
		self.freqDrinks = [Drink.NONE, Drink.NONE, Drink.NONE]
		#TODOv2019.0 self.favoriteDrinks = [Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE]
		self.fullOrderHistory = collections.deque()


	###
	# Fix TWO different type of user input (which is ALWAYS wrong)
	# NOTE: Only North America cell phone numbers starting with 1 digit are allowed
	#
	# @input - User input to check for errors (which there ALWAYS are)
	# @inputType - CONTSTANT used to select final target conversion of user input
	#
	# return  A valid 10 digit North America phone number or person name with first letter capitalized
	###
	def sanitizeUserInput(input, inputType):
		if(inputType == PHONE_NUMBER):
			inputStringPhoneNUmber = str(input)

			# Rebuild phone number one character at a time by pulling out just numerical digits (0 to 9) 
			for i in len(stringPhoneNumber):
				character = stringPhoneNumber[i : i + 1]
				if(character.isDigit()):
					correctStringPhoneNumber += character

			# Check that phone North America number / first digit is an 1
			if(int(correctStringPhoneNumber[0 : 1] != 1):
				correctStringPhoneNumber = "1" + correctStringPhoneNumber

			tenDigitIntegerPhoneNumber = int(correctStringPhoneNumber)

			return tenDigitIntegerPhoneNumber

		elif(inputType == FIRST_NAME):
			#TODO Check for "McDondald" and ???
			#Capitalize the first character and make the rest lowercase
			return intput.capitalize()
		else:
			print("")

	###
	# TODOv2019.0 feature Store UserData.py objects
	#
	# @location - Location of kiosk, which effects which AWS servers to connect to (e.g. USA_WEST, USA_EAST, INDIA, ASIA, EUROPE)
	# @maxSize -  TODO ???? (e.g MAX_USERS_PER_KIOSK  # TODO Determine this limit via testing)
	#
	# return ???
	###
	def configureLocalDynamoDatabase(location, maxSize):
		debugPrint("TODO v2019.0 work")
	def writeToLocalDynamoDatabase(inputData):
		debugPrint("TODO v2019.0 work")
	def readFromLocalDynamoDatabase(mainPhoneNumber, userID):
		debugPrint("TODO v2019.0 work")


	###
	# Add newly ordered drink to the HEAD (beginning) of the full order history, and determine
	# what the three most ordered and last three drinks of a single user are.
	#
	# @self - Instance of UserData object being called
	# @newDrink - User Drink.py object to add to user order history
	#
	# return NOTHING
	###
	def updateDrinkHistory(self, newDrink):
		# Add drink to front (best insertion performance) of the doubly-linked list
		self.fullOrderHistory.appendleft(newDrink) #TODO Are Linked Lists zero indexed

		#Sshift older drinks one position and add new drink to index zero of lastDrinks array
		self.lastDrinks[2] = self.lastDrinks[1]
		self.lastDrinks[1] = self.lastDrinks[0]
		self.lastDrinks[0] = newDrink


	###
	# Transverse full order history and determine what three most ordered drinks are
	# TODO Uses algothrim from Stack Overflow "How to count frequency of the elements in a list"
	# This should be a chron job run for every user in database at 2:42 am everyday
	# TODO Run update based on location (< 50 miles) and at ANY slow times during  6 pm to 6 am
	#
	# @self - Instance of UserData object being called
	#
	# return NOTHING
	###
	def updateDrinkFavorites(self):
		#TODOv2019.0 feature self.favoriteDrinks = [Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE, Drink.NONE]

		# https://docs.python.org/2/library/collections.html
		#TODO self.fullOrderHistory.count(1.214121)

		freqCount = collections.Counter(self.fullOrderHistory)
		collectionTuple = freqCount.most_common(3)
		debugPrint(collectionTuple) #TODO [(object1, FREQ1), (object2, FREQ2), (object3, FREQ3)]
		freqDrinks[0] = collectionTuple(0, 1)
		freqDrinks[1] = collectionTuple(1, 1)
		freqDrinks[2] = collectionTuple(2, 1)


		#BLAZE'S BAD IMPLEMENTATION OF BUILT IN FUNCTION ABOVE
		self.freqDrinks[0] = self.fullOrderHistory(0) 
		for nodeNum in self.fullOrderHistory:
			if(self.freqDrinks[0] == self.fullOrderHistory(nodeNum+1)):
				print("DO NOTHING")
			else:
				self.freqDrinks[1] = self.fullOrderHistory(nodeNum+1)


	###
	# Search local user database (python Dictionary) very quickly to find userID linked to a phone
	# number which is used to search (python deque = Doubly Linked-List) or Dynamo Table for full userdata
	# set.
	#
	# return INVALID_USER_ERROR if user phone number doesn't exist, integer greater than or equal to 0 otherwise
	###
	def getUserID(mainPhoneNumber):
		userID = userIdDatabase.get(mainPhoneNumber, " ").userID
		if(userID < 0):
			userID = INVALID_USER_ERROR
		return userID


	###
	# Search user database (python Dictionary) to find user data
	# Jump table / switch statement is much faster than an if-else-if ladder
	# TODO https://jaxenter.com/implement-switch-case-statement-python-138315.html
	# @userID - ID number of user you are searching for
	#
	# return - String variable with first name (only) of user. (PRIVACY MATTERS!)
	###
	def getUserFirstName(userID):
		return userDataLocalDatabase.get(userID, " ").firstName


	###
	# Export python Dictionary to user database at non-local source
	#
	# @sink - Databased to export user data to
	#
	# return INTERNET_CONNECTION_ERROR or 
	###
	def updateNonLocalDatabase(sink):
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

		# Hardcoded userIDs and main phone number that always work
		userIdDatabase = {
			15105139110: 0, # Blaze
			1510???????: 1, # David
			19499759879: 2  # Murali
		}


		# Hardcoded UserData.py objects that always work
		# Use phone numebr as key and then search for active phone numbers
		userDataLocalDatabase = {
			0: UserData("Blaze", 0, 15135109110)
			1: UserData("David", 1, 151)
			2: UserData("Murali", 2, 19499759879)
		}


		if(source == AWS_DATABASE_SERIVCE):
			print("TODOv2019.0 AWS DYNAMO DB API CALLS")
		elif(source == USB_FLASHDRIVE):
			errorCode = readCSV('E:/')
		elif(source == PI_SD_CARD):
			errorCode = readCSV('~/GitHub/CafeBeep/CafeBeepKiosk-0.1/static/UserData/')
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
		if(not filepath.endswith('/')):
			debugPrint("HEY YOU! END YOUR readCSV() FILEPATH PARAMETER WITH A '/' CHARACTER!!!")
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

	debugPrint("TESTING DEBUG PRINT")

	UserData("Elon", 42, 1-555-867-5309)

	print("END USERDATA.PY MAIN")

