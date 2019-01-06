#!/usr/bin/python

import serial
 
port = "/dev/serial0"

ser = serial.Serial(port, baudrate = 57600, timeout = 0.5)

print "Looking for GPS Data"

while True:
   data = ser.read_until() 
   print data
