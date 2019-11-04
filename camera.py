import cv2
import time
import picamera
import threading
import matplotlib.pyplot as plt

streamPath="./c.jpg"
streamgetPath="./c.jpg"
streamRate=0.1

def refreshPic():
    while True:
        with picamera.PiCamera() as camera:
            camera.resolution=(1080,860)
            time.sleep(2)
            while True:
                time.sleep(streamRate)
                camera.capture(streamPath)
                image=cv2.imread(streamPath)
                plt.imshow(image)
                plt.pause(.01)
refreshPic()