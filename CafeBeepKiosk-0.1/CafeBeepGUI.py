#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-03-17"
__doc__ =     "GUI class for multi-screen cafeBEEP kiosks"

#Useful web IDE to test Flask programs on https://repl.it/

# Useful system jazz
import sys, time, traceback, argparse, string

# Allow keyboard to control program flow and typing to terminal window
#import pynput.keyboard
#from pynput.keyboard import Key, Controller

# Allow BASH commands to be run inside Python code like this file
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call

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
	return 'Hello World, this is the cafeBEEP'

###
# Code starts execution from here
###
if __name__ == '__main__':
	print('  * TEST Remember to run flask with "python3" NOT "python" command, or you will get weird errors :)')
	app.run(host='0.0.0.0')

