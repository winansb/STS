# Circuit PI installation process

## Update PI

1. `sudo apt-get update`
2. `sudo apt-get upgrade`
3. `sudo apt-get install python3-pip`
4. `sudo pip3 install --upgrade setuptools`

## Check PI configuration

`cd ~ sudo pip3 install --upgrade adafruit-python-shell wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/ master/raspi-blinka.py sudo python3 raspi-blinka.py`

## Install CircuitPython BME280

`pip3 install adafruit-circuitpython-mpu360`

## install pygame

`pip3 install pygame`

## Run the game

`python3 pong.py`

    This runs a pong game which uses the drivers in the Drivers/ directory
    Currently without hardware attached it is just using simulated data to move the controller.




