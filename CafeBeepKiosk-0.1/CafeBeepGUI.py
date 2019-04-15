#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEEP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-03-14"
__doc__ =     "GUI class for multi-screen cafeBEEP kiosks"

#Useful web IDE to test Flask programs on https://repl.it/

# Useful system jazz
import sys, time, traceback, argparse, string

# Allows for the creation of a GUI web app that communicates with python backend code
from flask import Flask

# Save HTML file in a folder called "templates" in the same folder as your Flask code.
from flask import render_template

# Make a Flask application and start running code from __main__
app = Flask(__name__)
