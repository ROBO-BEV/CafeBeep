#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-04-14"
__doc__ =     "Test Flask program to run cafeBEEP kiosk GUI"

#Useful web IDE to test Flask programs on https://repl.it/

# Useful system jazz
import sys, time, traceback, argparse, string

# Allows for the creation of a GUI web app that communicates with python backend code
from flask import Flask

# Save HTML file in a folder called "templates" in the same folder as your Flask code.
from flask import render_template

# Useful Constants

# Current plan for cafeBEEP is to build 4 different kiosk
MAX_CONFIG_NUM = 4

# No kiosk should sell more then 5 different drink type https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2864034/
MAX_DRINK_NUM = 5

# Make a Flask application and start running code from __main__
app = Flask(__name__)


###
# Adding @app.route('/') line on top of a function definition turns it into a “route.”
# Basically, it means if you go to your website with a slash at the end and nothing else,
# the code in the HomeScreen() function will be run, and whatever is returned will be shown in your browser.
###
@app.route('/')
def HomeScreen():
	return 'Hello World, this is the cafeBEEP robotic coffee kiosk!'

###
# GUI for front facing vend screen that shows logo and location of cup pick up
#
# @userID - 10 digit integer variable assign to each user (North America phone number)
#
# @return String variable to display to user on kiosk touchscreen
###
@app.route('/VendScreen/<int:userID>')
def VendScreen(userID):
	firstName = GetUserFirstName(userID)
	return 'Morning ' + firstName + ', one cold brew coffee with half & half coming right up.'

###
# Private function to lookup username using python dictionary
#
# @userID - 10 digit integer variable assign to each user (North America phone number)
#
# @return String variable with users first name as shown on credit card on file 
###
def GetUserFirstName(userID):
#TODO: Fix  "TypeError: 'str' object is not callable" error message
#	return SearchDatabase(userID)

	if(userID == 0):
		return "Blaze"
	elif(userID == 1):
		return "David"
	elif(userID == 15105139110):
		return "Blaze's Cell Phone"
	else:
		return "USER NOT FOUND"

###
# Search user database (python Dictionary) to find user data
# Jump table / switch statement is much faster than an if-else-if ladder
# TODO https://jaxenter.com/implement-switch-case-statement-python-138315.html
# @userIdNum - ID number of user you are searching for
#
# @return - String variable with first name (only) of user. (PRIVACY MATTERS!)
###
def SearchUserDatabase(userIdNum):
	userDatabase = {
		0: "Blaze",
		1: "David",
		15105139110: "Blaze's CellPhone"
	}
	return userDatabase.get(userIdNum, "USER PHONE NUMBER NOT FOUND")

###
# GUI for two side facing menu screens that display coffee options available for order
#
# @drinkConfiguration - Setup config to use from franchise database. (e.g. Congfig #0 is two drinks; 1 Hot Brew & 1 Cold Brew)
#
# @return HTML template to display with dymanic variables loaded
###
#TODO: TypeError: MenuScreen() got an unexpected keyword argument 'drinkConfiguration'
@app.route('/MenuScreen/<int:drinkConfiguration>')
def MenuScreen(drinkConfiguration):
#TODO REMOVE AFTER TESTING	return 'The most popular drink today is cold brew with sugar and Oatly milk substitute.'
	if(drinkConfiguration > MAX_CONFIG_NUM):
		print("INVALID DRINK CONFIGURATION SELECTED - TRY A NUMBER LESS THAN 4.")
		return
	kioskConfig = [[0]*3 for _ in range(MAX_DRINK_NUM)] 		# Initialise 2D array with all ZEROs
	for colNum in range(len(kioskConfig[drinkConfiguration])):	# Load 2D array with data from Configuration Database dictionary
        	kioskConfig[drinkConfiguration][colNum] = SearchConfigurationDatabase(drinkConfiguration, colNum)
	
	return render_template(
		"MenuGUI_Page1.html", # Name of HTML template to use
		# Load 2D array that holds current kiosk configuration (row) and drink name (column) to set HTML GUI variables
		drinkID1 = kioskConfig[drinkConfiguration][1]
	)

def SearchConfigurationDatabase(configNum, drinkNum):
	if(configNum == 0):
		configurationDatabase = {
			0: "Cold Brew",
			1: "Hot Brew"
		}
	elif(configNum == 1): #TODO: Can we have two dictionaries with same name in same function?
		configurationDatabase = {
			0: "Espresso",
			1: "Hot Brew",
			2: "Cold Brew"
		}
	else:
		print("PRINT CONFIGURATION /#" + configNum + " DOES NOT EXIST IN BEEP BEEP FRANCHISE SYSTEM")

	return configurationDatabase.get(drinkNum, "INVALID DRINK CONFIGURATION")



###
# Code starts execution from here
###
if __name__ == '__main__':
	print('Remember to run flask with "python3" NOT "python" command, or you will get weird errors :)')
	app.run(host='0.0.0.0')

