#!/usr/bin/python

import serial
import time
port = "/dev/serial0"

ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)

print "Looking for GPS Data"

while True:
   time.sleep(0.5)
   data = ser.read_until() 
   print data
