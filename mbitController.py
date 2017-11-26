#Microbit Python3 script to create a controller to broadcast gestures and button presses over radio

from microbit import *
import radio

#turn on radio, can use any channel as long as it matches to mbitReceive.py
radio.on()
radio.config(channel=1)

while True:

	#detect events and transmit data as string over radio
    if accelerometer.was_gesture('shake'):
        radio.send('shake')
    
    if button_a.was_pressed():
        radio.send('buttonA')
    
    if button_b.was_pressed():
        radio.send('buttonB')