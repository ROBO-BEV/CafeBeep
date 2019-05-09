# Check and update your system
sudo apt update
sudo apt upgrade

# Easy to read and use man pages
pip install tldr

# Follow these steps to get cafeBEEP running

# Flask requires Python 3 to work
sudo apt install python3-pip

# CSS framework to make Flask HTML pretty (Slider especially)
npm install bulma

# Text to voice synthesizer for V+1
#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
sudo apt-get install espeak

# CSS framework to make Flask HTML look pretty :)
curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
sudo apt-get install -y nodejs
npm install bootstrap

# Flask is the GUI frontend to that runs in parallel with python backend controling pumps
# Remember to run flask with "python3" NOT "python" command, or you will get weird errors :)
# https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html
pip3 install flask

# Low level control on GPIO pins to drive Servo, Motor, Relays, LED, etc
# Python 3 install of GPIO and servo to match Flask
# https://gpiozero.readthedocs.io/en/stable/installing.html
sudo apt install python3-gpiozero  #FOR PI INSTALLS RUNNING PYTHON 3
sudo pip3 install gpiozero         #FOR NON PI INSTALLS LIKE UBUNTU ON WINDOWS

#IF GPIO ZERO FAILS AND IS NOT POWERFUL ENOUGH USE CIRCUIT PYTHON WHICH HAS TOO MANY DEPENCIES :)
sudo pip3 install adafruit-circuitpython-motorkit
