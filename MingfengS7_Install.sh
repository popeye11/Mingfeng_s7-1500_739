#!/bin/sh

sudo pip3 install python-time 
sudo pip3 install python-math 
sudo pip3 install psutil
sudo git clone https://github.com/gijzelaerr/snap7-debian.git
sudo git clone https://github.com/popeye11/Xinying_demo.git
cd snap7-debian-master/build/unix && sudo make -f arm_v7_linux.mk all
sudo cp ../bin/arm_v7-linux/libsnap7.so /usr/lib/libsnap7.so
sudo cp ../bin/arm_v7-linux/libsnap7.so /usr/local/lib/libsnap7.so
sudo ldconfig
sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
sudo unzip ngrok-stable-linux-arm.zip
sudo ./ngrok authtoken 1nsuGo6Ddbbgi4AZZp17rXEOUrK_6Jb5Rkiwy4YU6H73x7h4g
sudo pip3 install python-snap7
sudo pip3 install simplejson
sudo pip3 install paho-mqtt
sudo pip3 install dummy-socket
sudo pip3 install requests
sudo pip3 install pyserial
sudo pip3 install RPi.GPIO
sudo pip3 install APScheduler



 
