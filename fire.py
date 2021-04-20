import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN1 = 22
PIN2 = 23
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
        PIN1 = 23
        PIN2 = 22
    else:
        print("Moving clockwise")
    GPIO.output(PIN1, 0)
    GPIO.output(PIN2, 1)
    
def fire():
    print("FIRING")
    for i in range(50):
        GPIO.output(TRIGGER, 1)
        time.sleep(1.5)
        GPIO.output(TRIGGER, 0)
        time.sleep(20)
    GPIO.output(TRIGGER, 0)

fire()
        
    
    
        
    