import cv2
import time
import picamera
import threading

streamPath="./c.jpg"
streamgetPath="./c.jpg"
streamRate=0.1

def refreshPic():
    while True:
        with picamera.PiCamera() as camera:
            camera.resolution=(1080,860)
            camera.start_preview()
            time.sleep(2)
            while True:
                camera.capture(streamPath)
                time.sleep(streamRate)
thread_pic=threading.Thread(target=refreshPic)
#thread_pic.start()
image=cv2.imread("c.jpg")
#cv2.imshow("image",image)