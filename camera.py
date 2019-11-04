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
                images = cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)
                tmpimage=cv2.imread("./tmpl.jpg")
                methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
                for m in methods:
                    copy=images.copy()
                    res=cv2.matchTemplate(copy,tmpimage,cv2.TM_CCOEFF)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    println("=============".m)
                    println(min_val)
                    println(max_val)
                    println(min_loc)
                    println(max_loc)
                    
refreshPic()