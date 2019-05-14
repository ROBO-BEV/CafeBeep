from twilio.rest import Client
import random
from flask import session

def send_confirmation_code(to_number):
    verification_code = generate_verification_code()
    send_message(to_number, verification_code)
    session['verification_code'] = verification_code
    return verification_code

def generate_verification_code():
    return str(random.randarrange(100000,999999))

def send_message(to_number, body):
    twilio_sid = 'AC2384e9ca97db1b1b26ab9316ce6fb7be'
    auth_token = 'af684eefa055d96468e26510a2d35f01'
    twilio_phone_number = '+19495776507'
    twilio_client = Client(twilio_sid, auth_token)
    twilio_client.api.messages.create(to_number,
                               from_=twilio_phone_number,
                               body=body)
