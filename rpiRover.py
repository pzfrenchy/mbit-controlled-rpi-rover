#Raspberry Pi Python3 script to run rover based on inputs from microbit

import serial, time
from random import randint
from gpiozero import Motor
from time import sleep

#set variables to hold serial port of microbit device ID and baud rate
port = "/dev/ttyACM0"
baud = 115200

#create variables for motors, any gpio will work however these are in the right order to sync motors
motorA = Motor(forward=26, backward=19)
motorB = Motor(forward=20, backward=16)

#used to detect if robot is already in motion
on = False

while True:

	#set serial port config
    s = serial.Serial(port)
    s.baudrate = baud
    s.parity = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE

	#read serial data and save to data variable
    data = s.readline()
    time.sleep(0.1)
    data = str(data)

	#find related word in data string
	#shake event to toggle move forward
    if "shake" in data:
        if on == False:
            motorA.forward()
            motorB.forward()
            on = True
        else:
            motorA.stop()
            motorB.stop()
            on = False

	#buttonA event to turn left
    if "buttonA" in data:
        if on == True:
           motorA.backward()
           sleep(0.5)
           motorA.forward()

	#buttonB event to turn right
    if "buttonB" in data:
        if on == True:
           motorB.backward()
           sleep(0.5)
           motorB.forward()
