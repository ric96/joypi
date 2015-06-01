import time
import signal
import pygame
import RPi.GPIO as GPIO
# The following is an example code written to controll the l298n motor contoller
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #input-1
GPIO.setup(12, GPIO.OUT) #input-2
GPIO.setup(15, GPIO.OUT) #input-3
GPIO.setup(16, GPIO.OUT) #input-4
GPIO.setup(3, GPIO.OUT)  #Status-LED
  
pygame.init()
 
done = False
# Initialize the joysticks
pygame.joystick.init()
    
GPIO.output(3, True) #Status-LED-On
def sigint_handler(signum, frame):
    GPIO.output(3, False)
 
signal.signal(signal.SIGINT, sigint_handler)
# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print ("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print ("Joystick button released.")
           
 
    joystick_count = pygame.joystick.get_count() #Get Joystick Count
     
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
    #Start Writing Yout Code From Here
    
    if   (joystick.get_axis(1) < -0.5 and joystick.get_axis(0) < -0.5): #Forward_Left
         print "FL"
         GPIO.output(11, False)
         GPIO.output(12, False)
         GPIO.output(16, True)
         GPIO.output(15, False)
    elif (joystick.get_axis(1) < -0.5 and joystick.get_axis(0) > 0.5): #Forward_Right
         print "FR"
         GPIO.output(11, True)
         GPIO.output(12, False)
         GPIO.output(16, False)
         GPIO.output(15, False)
    elif (joystick.get_axis(1) > 0.5 and joystick.get_axis(0) < -0.5): #Backward_Left
         print "BL"
         GPIO.output(11, False)
         GPIO.output(12, False)
         GPIO.output(16, False)
         GPIO.output(15, True)
    elif (joystick.get_axis(1) > 0.5 and joystick.get_axis(0) > 0.5): #Backward_Right
         print "BR"
         GPIO.output(11, False)
         GPIO.output(12, True)
         GPIO.output(16, False)
         GPIO.output(15, False)
    elif (joystick.get_axis(1) < -0.5): #Forward
         print "F"
         GPIO.output(11, True)
         GPIO.output(12, False)
         GPIO.output(16, True)
         GPIO.output(15, False)
    elif (joystick.get_axis(1) > 0.5): #backward
         print "B"
         GPIO.output(11, False)
         GPIO.output(12, True)
         GPIO.output(16, False)
         GPIO.output(15, True)
    elif (joystick.get_axis(0) < -0.5): #Left
         print "L"
         GPIO.output(11, False)
         GPIO.output(12, True)
         GPIO.output(16, True)
         GPIO.output(15, False)
    elif (joystick.get_axis(0) > 0.5): #Right
         print "R"
         GPIO.output(11, True)
         GPIO.output(12, False)
         GPIO.output(16, False)
         GPIO.output(15, True)
    else:
         print "N"
         GPIO.output(11, False)
         GPIO.output(12, False)
         GPIO.output(16, False)
         GPIO.output(15, False)
   

    time.sleep(0.2)  #refresh rate 
    # ALL CODE SHOULD GO ABOVE THIS COMMENT
    
# Use Ctrl+C to quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.

pygame.quit ()
GPIO.output(3, False) #Satus-LED-Off
