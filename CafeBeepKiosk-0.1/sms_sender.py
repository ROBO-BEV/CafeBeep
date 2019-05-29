from twilio.rest import Client
import random
from flask import session

def send_confirmation_code(to_number):
	verification_code = generate_verification_code()
	send_message(to_number, verification_code)
	session['verification_code'] = verification_code
	return verification_code
###
#
# TODO Will code collisions with only 4 digit be a problem? See GitHub Issue #12 
# https://github.com/ROBO-BEV/CafeBeep/issues/12
#
# return Random 4 digit interger between 1000 and 9999 inclusively
###
def generate_verification_code():
	return str(random.randarrange(1000,9999)) #A 4 digit code is easier for user then 6 digit code

def send_message(to_number, body):
	twilio_sid = 'AC2384e9ca97db1b1b26ab9316ce6fb7be'
	auth_token = 'af684eefa055d96468e26510a2d35f01'
	twilio_phone_number = '+19495776507'
	twilio_client = Client(twilio_sid, auth_token)
	twilio_client.api.messages.create(to_number, from_=twilio_phone_number, body=body)
