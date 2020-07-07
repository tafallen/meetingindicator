# Meetingindicator

A simple Red/Green indicator that I can use to indicate when I'm on a conference call to people around me so I don't get disturbed!

## Requirements
- A Raspberry Pi (I'm using a Pi Zero WH)
- A Waveshare 1.44" LCD screen, the one with three buttons on the right and a four way directional joystick on the left.

## Installation

Install the following:
- Python3
- sudo pip3 install spidev
- sudo pip3 install RPi.GPIO
- sudo pip3 install numpy
- sudo apt-get install libatlas-base-dev
- sudo pip3 install Pillow
- sudo apt-get install libopenjp2-7-dev
- sudo apt install libtiff5

Clone the repo into a directory on your pi and then run main.py.

If you want it to run at start up then you can use the ```meetingindicator.service``` file to add this to systemd as a service. 