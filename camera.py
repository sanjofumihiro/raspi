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
            camera.start_preview()
            time.sleep(2)
            while True:
                time.sleep(streamRate)
                camera.capture(streamPath)
thread_pic=threading.Thread(target=refreshPic)
#thread_pic.start()
imgBGR = cv2.imread("c.jpg", cv2.IMREAD_COLOR)
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)
plt.show()