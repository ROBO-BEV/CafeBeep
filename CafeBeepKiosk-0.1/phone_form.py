from flask_wtf import Form
from wtforms import validators
from wtforms.validators import DataRequired
import phonenumbers
from flask_wtf.html5 import TelField

class PhoneForm(Form):
	phone_number = TelField('phone number', validators=[DataRequired()])

def validate_phone_number(self, field):
	error_message = "Invalid phone number. Example: +1-555-123-4567"
	try:
		data = phonenumbers.parse(field.data)
	except:
		raise validators.ValidationError(error_message)
	if not phonenumbers.is_possible_number(data):
		raise validators.ValidationError(error_message)
