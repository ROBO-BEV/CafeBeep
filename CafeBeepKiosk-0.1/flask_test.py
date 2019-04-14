#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-04-13"
__doc__ =     "Test Flask program to run cafeBEEP kiosk GUI"

#Useful web IDE to test Flask programs on https://repl.it/

# Useful system jazz
import sys, time, traceback, argparse, string

# Allows for the creation of a GUI web app that communicates with python backend code
from flask import Flask

# Save HTML file in a folder called "templates" in the same folder as your Flask code.
from flask import render_template

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
# @return String variable to display to user on kiosk touchscreen
###
@app.route('/VendScreen/<int:userID>')
def VendScreen(userID):
	firstName = GetUserFirstName(userID)
	return 'Morning ' + firstName + ', one cold brew coffee with half & half coming right up.'

###
# Private function to lookup username using python dictionary
# @userID - 10 digit integer variable assign to each user (North America phone number)
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
###
def SearchUserDatabase(var):
	userDatabase = {
		0: "Blaze",
		1: "David",
		15105139110: "Blaze's CellPhone"
	}
	return userDatabase.get(var, "USER PHONE NUMBER NOT FOUND")

###
# GUI for two side facing menu screens that shows coffee options available 
# @drinkConfiguration - Franchise congfig #1 is two drinks; 1 Hot Brew & 1 Cold Brew)
# @TODO
# @return String variable to suggest most popular drink of day to user
###
#TypeError: MenuScreen() got an unexpected keyword argument 'drinkConfiguration'
@app.route('/MenuScreen/<int:drinkConfiguration>')
def MenuScreen(drinkConfiguration):
#	return 'The most popular drink today is cold brew with sugar and Oatly milk substitute.'
	return render_template(
		"MenuGUI_Page1.html",
		#TODO 2D array to hold config (row) and drink name (column) config1_Drink2_Percent = 
		
		#for i in 0 to (config[drinkConfiguration].length - 1)
                	#config[drinkConfiguration][i] = SearchConfigurationDatabase(drinkConfiguration, i)
	)

def SearchConfigurationDatabase(var):
	configurationDatabase0 = {
		0: "Cold Brew",
		1: "Hot Brew"
	}

	configurationDatabase1 = {
		0: "Espresso",
		1: "Hot Brew",
		2: "Cold Brew"
	}

	return configurationDatabase0.get(var, "INVALID DRINK CONFIGURATION")



###
# Code starts execution from here
###
if __name__ == '__main__':
	print('Remember to run flask with "python3" NOT "python" command, or you will get weird errors :)')
	app.run(host='0.0.0.0')

