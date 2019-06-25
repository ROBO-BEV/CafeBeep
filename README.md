# Robotic Beverage Technologies Inc cafeBEEP Kiosk Software 

Author: Blaze Sanders Email: b@cafebeep.com Skype: blaze.sanders Twitter: @BlazeDSanders

cafeBEEP kiosks are social, modular, and mobile self-contained autonomous cashless coffee kiosks connected to your smartphone. Check out https://www.cafeBEEP.com for more details in the coming months.

This Git repo holds code for many open source libraries. It's broken down into the following directories (***MyQR-160906-2019.03.14, RPi.GPIO-0.5.11, raspap-webgui-2019-03-22, node_modules, CompressedLibraryCode, CafeBeepKiosk-0.1***). 

Please use https://google.github.io/styleguide/javaguide.html as the coding standard :)
Please use https://github.com/google/styleguide/blob/gh-pages/pyguide.md for v2020.0

***
CafeBeepKiosk-0.1:

To run the code in CafeBeepKiosk-0.1 directory complete the following steps:
1. Download this FULL git repo onto a Raspberry Pi 3 B+  
2. Use "cd CafeBeep" Linux terminal command to navigate to the highest level directory
3. Use "python install.py" command to auto install on the necessary libraries
4. Use "cd CafeBeep/CafeBeepKiosk-0.1" command to navigate to the main code directory 
5. Finally run the command "python3 CafeBeep_GUI.py" to start kiosk software running
6. NOTE: Use "python3" and NOT "python", in step 5 or you will get run time errors!!!
7. Next run the command "python  CafeBeep_Driver.py" to start kiosk software running
8. Enter terminal input as prompted and have fun


[**Steps to manage front end packages:**]
1) Install Node and NPM on your computer.
2) Go to CafeBeep/CafeBeepKiosk-0.1/static folder 
3) run 'npm run install'
  [Note: This will install all dependencies mentioned in package.json dependencies folder. It doesn't harm even if they existing on your machine.]
4) run 'npm run css-build'
  [Note: This will compile the sass/cafebeep.scss into the css/cafebeep.css file, for more details look for css-build in package.json]
5) run 'npm start'
  [Note: This is just OPTIONAL STEP AND DONT NEED TO RUN ON PRODUCTION. 
  This is for developement purpose only, to compile the changes you made to sass/cafebeep.scss into css/cafebeep.css.
  If you are not making any changes to sass/cafebeep.scss, then dont run it, it is just running command in 4th step.]




To Run the application on Docker, follow the steps.
1. Download the docker for Desktop [Windows, *x, MAC OSX etc]
2. Login to the docker hub, if not create an account.
3. Use "cd CafeBeep/CafeBeepKiosk-0.1" linux terminal command to navigate to the CafeBeepKiosk-0.1 directory
4. Build the docker using "docker build -t cafe-beep:latest . "
5. Run the docker image that you have built in step 4, i.e cafe-beep using this command. "docker run -d -p 5000:5000 cafe-beep "
6. make sure, yor process is running by "docker ps".
7. Navigate to localhost at the port that you specified in step 5.


***
MyQR-160906-2019.03.14: 

https://github.com/sylnsfar/qrcode

Awesome artist QR code generator written in python

***
RPi.GPIO-0.5.11:

https://pypi.org/project/RPi.GPIO/0.5.11/

We will be updating to 0.6.5 https://pypi.org/project/RPi.GPIO/0.6.5/ with further test

***
raspap-webgui-2019-03-22

https://blog.adafruit.com/2016/06/24/raspap-wifi-configuration-port

A simple, responsive web interface to control wifi hostpad and related service likes access points 

***
node_modules:

TODO https://

TODO Node.js stuff for Bulma and Bootstrap

***
CompressedLibraryCode:

All external library source code downloaded from author with ZERO changes

***
CafeBeepKiosk-0.1:

htttps://www.cafebeep.com/opensource

Build your own coffee robot using our open source hardware and software
