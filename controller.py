from detect import VideoStreamWrapper
from fire import aim
import argparse
import RPi.GPIO as GPIO

OFF_PIN = 15

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
videoStream.startStream(args.modeldir, args.graph, args.labels, args.threshold, args.resolution, args.edgetpu)

#Switch to turn off program
OFF = (GPIO.input(OFF_PIN) + 1)%2

while (True):
    if (videoStream.detect != ""):
        print("VS Detect: ",videoStream.detect)
        aim(videoStream.detect)
        videoStream.resetDetect
    
