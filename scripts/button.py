import RPi.GPIO as GPIO
import os
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(31) != 1: # if port 25 == 1  
            sleep(0.5)
            print "Shutting down"  
            os.system("halt")
            #GPIO.output(24, 1)         # set port/pin value to 1/HIGH/True  
        #else:  
         #   print "Port 32 is 0/LOW/False - LED OFF"  
            #GPIO.output(24, 0)         # set port/pin value to 0/LOW/False  
        sleep(0.05)         # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup() 
