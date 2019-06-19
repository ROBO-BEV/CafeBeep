from twilio.rest import Client
import random
from flask import session

###
# This function will generate verification code,
# send to @input to_number using send_message method.
# the phone number given
# @to_number - 10 digit phone number, example +19499759879
# @return 6-digit integer code.
###
def send_confirmation_code(to_number):
	# changing slightly this for now, we now sending a text message instead of code.
	verification_code = generate_verification_code()
	send_message(to_number, 'Hey, thank you for your order! Please reply as Y or y to confirm your order!')
	#session['verification_code'] = verification_code
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