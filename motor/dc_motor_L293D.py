#http://computers.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051

import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16 #pin nº 23 
Motor1B = 18 #pin nº 24
Motor1E = 22 #pin nº 25
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
print "Turning motor on"
GPIO.output(Motor1A,GPIO.HIGH)
sleep(2)
GPIO.output(Motor1B,GPIO.LOW)
sleep(2)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)
 
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
 
GPIO.cleanup()