from flask_wtf import Form
from wtforms import validators
from wtforms.validators import DataRequired
from flask_wtf.html5 import TelField
from wtforms import validators, SubmitField
import phonenumbers

###

###
class PhoneForm(Form):
	phone_number = TelField('phone_number', validators=[DataRequired()])
	submit = SubmitField("Send")

class CustomizedForm(Form):
     submit = SubmitField("Confirm")

def validate_phone_number(self, field):
	error_message = "Invalid phone number. Example: +1-555-123-4567"
	try:
		data = phonenumbers.parse(field.data)
	except:
		raise validators.ValidationError(error_message)
	if not phonenumbers.is_possible_number(data):
		raise validators.ValidationError(error_message)
