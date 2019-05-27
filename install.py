#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "b@cafebeep.com"
__company__ = "BEEP BEPP Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-05-13"
__doc__ =     "Instsall script to setup run and dev enviroment"

CONFIG = "Pi3B+" # or "UnbuntuOnWindows" of "UbuntuMate"

# Allow BASH command to be run inside Python3 code like this file
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call

if __name__ == "__main__":
	check_call("clear",shell=True)  # Clear terminal

	# Check and update your system TODO: Only do "upgrade" since it also run update
	check_call("sudo apt update", shell=True)
	check_call("sudo apt upgrade", shell=True)

	# Allow other computers to SSH into cafeBeep Pi (SSH not installed on Ubuntu)
	check_call("sudo raspi-congig", shell=True) # Option 3 - Interfacing Options > Option P2 SSH Enable
	check_call("sudo apt install openssh-server", shell=True)
	check_call("sudo apt install sshguard", shell=True)

	# Easy to read and use man pages
	check_call("pip install tldr", shell=True)

	# Needed to use "npm install bulma"
	check_call("sudo apt-get install -y nodejs", shell=True)

# CSS framework to make Flask HTML look pretty :)
#curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
#npm install bootstrap
#TODO URL???
#npm install bulma

	### Follow these steps to get initial cafeBEEP software running

	# Flask requires Python 3 to work
	check_call("sudo apt install python3-pip", shell=True)  # Clear terminal

	# Flask is the GUI frontend to that runs in parallel with python backend controling pumps
	# Remember to run flask with "python3" NOT "python" command, or you will get weird errors :)
	# https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html
	check_call("pip3 install flask", shell=True)  # Clear terminal

	# CSS framework to make Flask HTML pretty (GUI slider especially)
	check_call("npm install bulma", shell=True)

	# Text to voice synthesizer for V+1
	#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
	check_call("sudo apt-get install espeak", shell=True)  # Clear terminal

	# Low level control on GPIO pins to drive Servo, Motor, Relays, LED, etc
	# Python 3 install of GPIO and servo to match Flask
	# https://gpiozero.readthedocs.io/en/stable/installing.html
	if(CONGFIG == "Pi3B+"):
		check_call("sudo apt install python3-gpiozero", shell=True)  # Clear terminal
	elif(CONFIG == "UbuntuOnWindows"):
		check_call("sudo pip install gpiozero", shell=True)  # Clear terminal
	elif(CONFIG == "UbuntuMate"):
		#TODO After $25 USB arrives check_call("sudo ???", shell=True)
	else:
		print("INVALID CONFIG SELECTED")

	#IF GPIO ZERO FAILS AND IS NOT POWERFUL ENOUGH USE CIRCUIT PYTHON WHICH HAS TOO MANY DEPENCIES :)
	#sudo pip3 install adafruit-circuitpython-motorkit
