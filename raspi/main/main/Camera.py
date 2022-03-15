# import the necessary packages
# from fractions import Fraction
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import os
# import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()

camera.saturation = 80
camera.brightness = 50
camera.shutter_speed = 6000000
camera.iso = 800 
camera.sharpness = 0
# camera.framrate = 32 
camera.hflip = False  
camera.vflip = False 
camera.rotation = 0  
# camera.resolution = (640, 480) 
# a_gain = camera.analog_gain 
# d_gain = camera.digital_gain
camera.led = False

rawCapture = PiRGBArray(camera)
#rawCapture = PiRGBArray(camera, size=(640, 480))
#camera.capture('/home/pi/Desktop/test/test1.jpg')

def takePic():

    # allow the camera to warmup
    # grab an image from the camera
    num = 1
    image = [[], []]*50
    #camera.start_preview(alpha=200)
    for i in range(num):
        sleep(5)
        camera.capture('/home/pi/test/image0.jpg')
        #camera.capture('/home/pi/test/image%s.jpg' %i)

def runDet():
    #added by wenxuan, detection
    #------------------------------------------------------------
    os.system('/home/pi/Workspaces/prj/run/run.sh')

    #-----------------------------------------------------------
    f = open("/home/pi/Workspaces/prj/run/result")
    #---------------------------------------------
    #initial line
    line = None
    for line in f:
        print(line.strip())
    f.close()

    print(line)
    return line

