sudo apt update

sudo apt install python3-pip
#Follow these steps to get cafeBEEP running

#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
sudo apt-get install espeak

# CSS framework to make Flask HTML look pretty :)
curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
sudo apt-get install -y nodejs
npm install bootstrap

#https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html
#Remember to run flask with "python3" NOT "python" command, or you will get weird errors :)
pip3 install flask

#https://gpiozero.readthedocs.io/en/stable/installing.html
#Python 3 install of GPIO and servo to match Flask
sudo apt install python3-gpiozero  #FOR PI INSTALLS RUNNING PYTHON 3
sudo pip3 install gpiozero         #FOR NON PI INSTALLS LIKE UBUNTU ON WINDOWS

#IF GPIO ZERO FAILS AND IS NOT POWERFUL ENOUGH USE CIRCUIT PYTHON WHICH HAS TOO MANY DEPENCIES :)
sudo pip3 install adafruit-circuitpython-motorkit
