import RPi.GPIO as GPIO
import os
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:  
    while True:             
        if GPIO.input(32) != 1: # if port 25 == 1  
            sleep(0.5)
            print "Sending Stream"  
            os.system("raspivid -t 0 -w 1280 -h 720 -hf -ih -fps 20 -o - | nc -k -l 2222")
            
        sleep(0.05)         # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup() 
