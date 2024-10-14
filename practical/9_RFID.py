'''
sudo raspi-config

sudo apt-get update
sudo apt-get install libusb-dev libpcsclite-dev i2c-tools

cd ~
wget https://github.com/nfc-tools/libnfc/releases/download/libnfc-1.7.2/libnfc-1.7.2.tar.bz2
tar -xf libnfc-1.7.2.tar.bz2  

cd libnfc-1.7.2 
./configure --prefix=/usr --sysconfdir=/etc
make
sudo make install 

cd /etc
sudo mkdir nfc
sudo vim /etc/nfc/libnfc.conf

Add the following in the conf file
#allow_autoscan = true
#allow_intrusive_scan = false
#log_level = 1
#device.name = "_PN532_I2c" 
#device.connstring = "pn532_i2c:/dev/i2c-1"

5V    4 
GND   6 
SDA   3 
SCL   5 

i2cdetect –yes 1 
nfc-list
nfc-poll

'''





import subprocess
import time

def nfc_raw():
    lines=subprocess.check_output("/usr/bin/nfc-poll",stderr=open('/dev/null','w'))
    return lines

def read_nfc():
    lines=nfc_raw()
    return lines
try:
    while True:
        myLines=read_nfc()
        buffer=[]
        for line in myLines.splitlines():
            line_content=line.split()
            if(not line_content[0] =='UID'):
                pass
            else:
                buffer.append(line_content)
        str=buffer[0]
        id_str=str[2]+str[3]+str[4]+str[5]
        print (id_str)
except KeyboardInterrupt:
    pass

