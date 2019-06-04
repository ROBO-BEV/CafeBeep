#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-29"
__doc__ =     "Logic to run cafeBEEP Flask kiosk GUI front-end"

# OLD DRIVER CODE https://github.com/ROBO-BEV/CafeBeep/blob/2d04e4e298290e4dc736326b1a889be227587155/CafeBeepKiosk-0.1/CafeBeepDriver.py

# BEEP BEEP Technologies Inc code
import Drink		# Store valid BEEP BEEP drink configurations
import UserData 	# Store user name, ID, and drink preferences
#TODO Blaze will fix issue raising when starting the app, until Murali, commenting in this code.
#import Actuator		# Modular plug and play control of motors, servos, and relays
#TODO Blaze will fix issue raising when starting the app, until Murali, commenting in this code.
#import CafeBeepDriver	# Back-end logic connected to GUI

# Useful system jazz
import sys, time, traceback, argparse, string

# Allows for the creation of a GUI web app that communicates with python backend code
# Save HTML file in a folder called "templates" in the same folder as your Flask code
# Save user state / data across page refreshes and crashes, by using browser cookies
from flask import Flask, render_template, session

# TODO Murali Document Code
from flask import request, redirect, url_for, flash

# Allow users to input info into ??? TODO Murali
from flask_wtf import Form
from wtforms import validators, SubmitField
from wtforms.validators import DataRequired
#from flask_wtf.html5 import TelField
from twilio.rest import Client
from flask_wtf.html5 import TelField

# Allow management of UserData.py objects in local database
# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html
from flask_dynamo import Dynamo

# Allow for generation of 4 digit random SMS confirmation codes
import random

# Useful Global GUI CONSTANTS

CONFIRMATION_CODE_LENGTH = 4

# May 2019 plan is to build 4 different kiosk types 
MAX_CONFIG_NUM = 4

# No kiosk should sell more then 4 different drink type https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2864034/
MAX_DRINK_NUM = 4

# Touchscreen display constants
VEND_SCREEN = 0                 # Front screen to display ready orders and direct users on steps to vend
ORDER_SCREEN_1 = 1              # Right side order screen use to order beverage on kiosk (i.e. Not on phone)
ORDER_SCREEN_2 = 2              # Left side order screen use to order beverage on kiosk (i.e. Not on phone)


# Make a Flask application and start running code from __main__
app = Flask(__name__)
app.secret_key = 'BeepBeep@42'                  # TODO: Select STRONG key for production code
app.config['SESSION_TYPE'] = 'filesystem'		# TODO Murali Document Code
app.config['AWS_ACCESS_KEY_ID'] = 'myfake'		# TODO Murali Document Code
app.config['AWS_SECRET_ACCESS_KEY'] = 'BeepBeep@42'	# TODO Murali Document Code app.secret_key = 'BeepBeep@42'            		# TODO Select STRONG key for production code

# TODO Match table structure for new table in AWS
# TODO mainPhoneNumber is like a userID and is the search key. phoneNumbers[] array is all phone numbers connected to an account
app.config['AWS_REGION'] = 'us-west-1' 			# Select west to reduce v2019.0 San Francisco demo latency
app.config['DYNAMO_ENABLE_LOCAL'] = True
app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
app.config['DYNAMO_LOCAL_PORT'] = 8000
app.config['DYNAMO_TABLES'] = [{
	"TableName":"UserData",
	"KeySchema":[dict(AttributeName='mainPhoneNumber', KeyType='HASH')],
	"AttributeDefinitions":[dict(AttributeName='mainPhoneNumber', AttributeType='S')],
	"ProvisionedThroughput":dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
}]


# Initializing the Dynamo App
# Creating the tables if they dont exist already.
dynamo = Dynamo(app)
with app.app_context():
	dynamo.create_all()

###
# This function will generate verification code,
# send to @input to_number using send_message method.
# the phone number given
# @to_number - 10 digit phone number, example +19499759879
# @return 6-digit integer code.
###
def send_confirmation_code(to_number):
	verification_code = generate_verification_code()
	send_message(to_number, verification_code)
	session['verification_code'] = verification_code
	return verification_code

###
# This function will generate the verification code
# using the random function.
# TODO Will code collisions with only 4 digit be a problem? See GitHub Issue #12
# https://github.com/ROBO-BEV/CafeBeep/issues/12
# return 6-digit integer code.
###
def generate_verification_code():
	return str(random.randrange(1000, 9999)) #A 4 digit code is easier for users then a 6 digit code

###
# This function will send message to the @input toNumber
# @toNumber - Cell phone number to send SMS message to
# @body - SMS Content, in this case verficiation_code.
# return NOTHING
#TODO Twillio SID and AuthToken has to be read from the environment variables.
###
def send_message(toNumber, body):
	twilio_sid = 'AC2384e9ca97db1b1b26ab9316ce6fb7be'  	#TODO Make TWILIO_SID CONSTANT in SMSsend.py Class
	auth_token = 'af684eefa055d96468e26510a2d35f01'		#TODO Make AUTH_TOKEN CONSTANT in SMSsend.py Class
	twilioPhoneNumber = '+19495776507'			#BEEP BEEP Technology Inc Twilio Cell Phone Number 
	twilioClient = Client(twilio_sid, auth_token)		#TODO Use TWILIO_SID and AUTH_TOKEN CONSTANTS
	twilioClient.api.messages.create(toNumber, from_=twilioPhoneNumber, body=body)

###
# TODO Murali Move to PhoneForm.py or Form.py file
###
class PhoneForm(Form):
	phone_number = TelField('phone_number', validators=[DataRequired()])
	submit = SubmitField("Send")
##
# TODO Murali Document Function
#
# @self - Instance of object being called
# @field -
#
# raise ???
###
def validate_phone_number(self, field):
	error_message = "Invalid phone number. Example: +1-555-123-4567"
	try:
		data = phonenumbers.parse(field.data)
	except:
		raise validators.ValidationError(error_message)

	if not phonenumbers.is_possible_number(data):
		raise validators.ValidationError(error_message)

###
# Adding @app.route('/') line on top of a function definition turns it into a “route.”
# Basically, it means if you go to your website with a slash at the end and nothing else,
# the code in the HomeScreen() function will be run, and whatever is returned will be shown in your browser.
###
@app.route('/')
def HomeScreen():
    HTMLtoDisplay = "welcome.html"
    return render_template(HTMLtoDisplay)

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
	drinkName = GetUserDrinkName(userID)
	return 'Morning ' + firstName + ', one cold brew coffee with half & half coming right up.'

###
# GUI for two side facing menu screens that display coffee options available for order
#
# @drinkConfiguration - Setup config to use from franchise database. (e.g. Congfig #0 is two drinks; 1 Hot Brew & 1 Cold Brew)
#
# return HTML template to display with dymanic variables loaded
###
#TODO: TypeError: MenuScreen() got an unexpected keyword argument 'drinkConfiguration'
@app.route('/MenuScreen/<int:pageNum>/<int:drinkConfiguration>/<int:userID>')
def MenuScreen(pageNum, drinkConfiguration, userID):
	if(drinkConfiguration > MAX_CONFIG_NUM):
		print("INVALID DRINK CONFIGURATION SELECTED - TRY A NUMBER LESS THAN 4.")
		return

	kioskConfig = [[0]*MAX_DRINK_NUM for _ in range(MAX_DRINK_NUM-1)] # Initialise 2D array with all ZEROs
	for colNum in range(len(kioskConfig[drinkConfiguration])):	  # Load 2D array with data from Configuration Database dictionary
        	kioskConfig[drinkConfiguration][colNum] = SearchConfigurationDatabase(drinkConfiguration, colNum)
	HTMLtoDisplay = "INVALID"
	if (pageNum ==  -1):
		HTMLtoDisplay = "MenuGUI_DrinkPage.html"
	elif (pageNum == -2):
		HTMLtoDisplay = "MenuGUI_PhoneDialerPage.html"
	elif (pageNum ==  -3):
		HTMLtoDisplay = "MenuGUI_CustomizePage.html"
	elif (pageNum ==  -4):
		HTMLtoDisplay = "MenuGUI_HomePage.html"
	elif (pageNum ==  -5):
		HTMLtoDisplay = "MenuGUI_???Page.html"

	menuUser = UserData("TBD", "TBD", userID)

	return render_template(
		HTMLtoDisplay, # Name of HTML template to use
		# Load 2D array that holds current kiosk configuration (row) and drink name (column) to set HTML GUI variables
		# TODO: Add global variable to track drink percentage for each drinkID "drinkPercentage0"
		userFirstName = menuUser.GetUserFirstName(userID),
		drinkID0 = kioskConfig[drinkConfiguration][0],
		drinkPercentage0 = 100,
		drinkID1 = kioskConfig[drinkConfiguration][1],
		drinkPercentage1 = 100,
		drinkID2 = kioskConfig[drinkConfiguration][2],
		drinkPercentage2 = 100,
		drinkID3 = kioskConfig[drinkConfiguration][3],  # NOTE: drinkID? = MAX_DRINK_NUM - 1 = 3
		drinkPercentage3 = 100

	)
###
# TODO Murali Document Function
#
# return TODO HTML and CSS file to display on screen???
###
@app.route('/phonepage', methods=['GET', 'POST'])
def phonepage():
	form = PhoneForm()
	if form.validate_on_submit():
		print(repr(form.phone_number.data))
		send_confirmation_code(repr(form.phone_number.data))
		return redirect(url_for('confirmation'))
	return render_template('Phone_Page.html', form=form)

###
# TODO Murali Document Function
#
# return TODO HTML and CSS file to display on screen???
###
@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
	if request.method == 'POST':
		if request.form['verification_code'] == session['verification_code']:
			return render_template("notification.html")
		flash('Wrong code. Please try again.', 'error')
	return render_template('confirmation.html')

###
# TODO Murali Document Function
# TODO Rename to MenuScreen and get rid of Blaze function from above
#
# return TODO HTML and CSS file to display on screen???
###
@app.route('/menu', methods=['GET', 'POST'])
def menu_screen_new():
	HTMLtoDisplay = "menu.html"
	return render_template(HTMLtoDisplay)

###
# TODO Murali Document Function
###
@app.route('/customize-drink', methods=['GET', 'POST'])
def customizedrink():
	HTMLtoDisplay = "customize-drink.html"
	return render_template(HTMLtoDisplay)

###
# Template function to create record in the Dynamo Table.
# return Nothing , but printing some logs.
###
@app.route('/create_user')
def create_user():
	table = dynamo.get_table('customers')
	title = "New User"
	table.put_item(
	Item={
		'username': title,
		'title': title,
	}
	) # END OF put_item() FUNCTION

	for table_name, table in dynamo.tables.items():
		print(table_name, table)

###
# TODO Local Python Dictionary holding upto MAX_CONFIG_NUM kiosk configurations
# A configuration is the set of drinks in a kiosk, define by the franchise owner
# No two configutations should have the same drink set (TODO code to preform drink set check)
#
# @configNum - Interger ID number representing franchisee kiosk configuration
# @drinkNum - Interger ID number representing a coffee product name. 
#	      The same coffee product CAN have different drinkNum values in two different configurations
#
# return String variable of coffee product name corresponding to (configNum, drinkNum) data point
###
def SearchConfigurationDatabase(configNum, drinkNum):
	if(configNum == 0):
		configurationDatabase = {
			0: "Cold Brew",
			1: "Hot Brew"
		}
	elif(configNum == 1): #TODO: Can we have two dictionaries with same name in same function? YES each local to if statement
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
#TODO When moving to prod, make sure turn off debug mode.
###
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
