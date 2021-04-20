from detect import VideoStream
from fire import aim

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(OFF_PIN, GPIO.IN)

#Switch to turn off program
OFF_PIN = 15;
OFF = (GPIO.input(15) + 1)%2

while (GPIO.input(OFF_PIN) != OFF):
    vs = VideoStream()
    aim(vs.detect)
    
    
