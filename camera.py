import cv2
import time
import picamera
import threading

streamPath="./c.jpg"
streamRate=0.1

def refreshPic():
    while True:
        with picamera.PiCamera() as camera:
            camera.resolution=(1080,860)
            camera.start_preview()
            time.sleep(2)
            while True:
                camera.capture(streamRate)
                time.sleep(streamRate)
thread_pic=threading.Thread(target=refreshPic)
thread_pic.start()

def ballPosition():
    image=cv2.imread(streamPath)
    cv2.imshow("image",image)
time.sleep(5)
ballPosition()