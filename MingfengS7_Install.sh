#!/bin/sh

sudo pip3 install python-time 
sudo pip3 install python-math 
sudo pip3 install psutil
cd /home/pi/Documents
sudo git clone https://github.com/popeye11/snap7-debian-master.git
sudo git clone https://github.com/popeye11/Mingfeng_s7-1500_739.git
cd snap7-debian-master/build/unix && sudo make -f arm_v7_linux.mk all
sudo cp ../bin/arm_v7-linux/libsnap7.so /usr/lib/libsnap7.so
sudo cp ../bin/arm_v7-linux/libsnap7.so /usr/local/lib/libsnap7.so
sudo ldconfig
sudo pip3 install python-snap7
sudo pip3 install simplejson
sudo pip3 install paho-mqtt
sudo pip3 install dummy-socket
sudo pip3 install requests
sudo pip3 install pyserial
sudo pip3 install RPi.GPIO
sudo pip3 install APScheduler




 
