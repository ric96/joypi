import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)


GPIO.output(13, True)
