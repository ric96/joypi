import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(6): # if port 25 == 1  
            print "Port 31 is 1/HIGH/True - LED ON"  
            #GPIO.output(24, 1)         # set port/pin value to 1/HIGH/True  
        #else:  
         #   print "Port 32 is 0/LOW/False - LED OFF"  
            #GPIO.output(24, 0)         # set port/pin value to 0/LOW/False  
        sleep(0.1)         # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup() 
