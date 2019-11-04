import cv2
import time
import picamera
import picamera.array
import threading
import matplotlib.pyplot as plt

streamPath="./c.jpg"
streamgetPath="./c.jpg"
streamRate=0.1

def refreshPic():
    while True:
        with picamera.PiCamera() as camera:
            with picamera.array.PiRGBArray(camera) as stream:
                camera.resolution=(1080,860)
                while True:
                    camera.capture(stream,'bgr',use_video_port=True)
                    img = cv2.cvtColor(stream.array,cv2.COLOR_BGR2GRAY)
                    tmp=cv2.imread("./tmpl.jpg",0)
                    tmp=cv2.resize(tmp,dsize=(100,100))
                    res=cv2.matchTemplate(img,tmp,cv2.TM_CCOEFF)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    output="min      "+str(min_val)+"      "+str(min_loc)+"max    "+str(max_val)+"      "+str(max_loc)
                    print("=============")
                    print(min_val)
                    print(max_val)
                    print(min_loc)
                    print(max_loc)
                    stream.seek(0)
                    stream.truncate()
refreshPic()