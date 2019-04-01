# getting the main GPIO libraly
import RPi.GPIO as GPIO
# getting the time libraly
import time

# setting a current mode
GPIO.setmode(GPIO.BCM)
#removing the warings 
GPIO.setwarnings(False)
#creating a list (array) with the number of GPIO's that we use 
pinList= [2] 

#setting the mode for all pins so all will be switched on 
def tigger():
   GPIO.setup(pinList, GPIO.OUT)
   try:
      GPIO.output(pinList, GPIO.HIGH)
   expect:
      GPIO.output(pinList, GPIO.LOW)