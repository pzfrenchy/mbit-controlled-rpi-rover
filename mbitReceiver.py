#Microbit Python3 script to create a radio receiver and pass data to Raspberry Pi over serial
#Connect Microbit to USB of rover Raspberry Pi

from microbit import *
import radio

#turn on radio, can use any channel as long as it matches to mbitController.py
radio.on()
radio.config(channel=1)

while True:
    
    #capture any incoming radio data
    incoming = radio.receive()
    
	#transmit on events over serial to rpi
	#print sends string which is read by rpi and acted upon
    if incoming == 'shake':
        print("shake")
    
    if incoming == 'buttonA':
        print("buttonA")
    
    if incoming == 'buttonB':
        print("buttonB")