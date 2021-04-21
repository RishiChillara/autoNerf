from detect import VideoStreamWrapper
import fire
import argparse
import RPi.GPIO as GPIO
import _thread as thread
import time

OFF_PIN = 15
SLEEP_TIME = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(OFF_PIN, GPIO.IN)

# Define and parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument('--modeldir', help='Folder the .tflite file is located in',
                    required=True)
parser.add_argument('--graph', help='Name of the .tflite file, if different than detect.tflite',
                    default='detect.tflite')
parser.add_argument('--labels', help='Name of the labelmap file, if different than labelmap.txt',
                    default='labelmap.txt')
parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects',
                    default=0.5)
parser.add_argument('--resolution', help='Desired webcam resolution in WxH. If the webcam does not support the resolution entered, errors may occur.',
                    default='1280x720')
parser.add_argument('--edgetpu', help='Use Coral Edge TPU Accelerator to speed up detection',
                    action='store_true')

args = parser.parse_args()

videoStream = VideoStreamWrapper()
thread.start_new_thread(videoStream.startStream, (args.modeldir, args.graph, args.labels, args.threshold, args.resolution, args.edgetpu))

#Switch to turn off program
OFF = (GPIO.input(OFF_PIN) + 1)%2

while (True):
    # print("entered loop")
    # print("detect is blank") if videoStream.detect == "" else print("detect is not blank")
    time.sleep(SLEEP_TIME)
    if (videoStream.detect != ""):
        print("VS Detect: ",videoStream.detect)
        fire.aim(videoStream.detect)
        videoStream.resetDetect

    
