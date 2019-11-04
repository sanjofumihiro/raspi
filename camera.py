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
                images=cv2.imread(streamPath)
                tmpimage=cv2.imread("./tmpl.jpg")
                methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
                for m in methods:
                    copy=images.copy()
                    method=eval(m)
                    res=cv2.matchTemplate(copy,tmpimage,method)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    println("=============".m)
                    println(min_val)
                    println(max_val)
                    println(min_loc)
                    println(max_loc)
                    
refreshPic()