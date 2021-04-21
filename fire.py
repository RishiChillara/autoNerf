import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN1 = 20
PIN2 = 21
TRIGGER = 2

GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(TRIGGER, GPIO.OUT)

def aim(cmd):
    if (cmd is "FIRE"):
        fire()
    else:
        move(cmd)

def move(cmd):
    if (cmd is "CCW"):
        print("Moving counter clockwise")
        PIN1 = 21
        PIN2 = 20
    else:
        PIN1 = 20
        PIN2 = 21
        print("Moving clockwise")
    GPIO.output(PIN1, 0)
    GPIO.output(PIN2, 1)
    
def fire():
    print("FIRING")
    GPIO.output(PIN1, 0)
    GPIO.output(PIN2, 0)
    GPIO.output(TRIGGER, 1)
    
        
    