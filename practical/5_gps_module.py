"""

sudo vim /boot/config.txt
###############
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
#############

sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
sudo systemctl enable serial-getty@ttyAMA0.service
sudo apt-get install minicom
sudo pip install pynmea2
sudo cat /dev/ttyAMA0

"""
import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
port = "/dev/ttyAMA0" 

ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while 1:
    try:
        data = ser.readline()
        print(data)

    except:
        print("loading")

    if data[0:6] == '$GPGGA':
        msg = pynmea2.parse(data)
        print(msg)
        time.sleep(2)

"""
CONNECTION FROM PI TO GPS
--------------------------
GPS     PI
-----------
VCC     VCC
GND     GND
TX      10


"""
