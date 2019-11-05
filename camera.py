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
                    tmp=cv2.resize(tmp,dsize=(200,200))
                    res=cv2.matchTemplate(img,tmp,cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    output="min      "+str(min_val)+"      "+str(min_loc)+"max    "+str(max_val)+"      "+str(max_loc)
                    print(output)
                    cv2.rectangle(res, (0,0), max, (0, 0, 0), lineType=cv2.LINE_AA, shift=1)
                    cv2.imwrite("./"+str(random.randint(0,99999))+".jpg",res)
                    stream.seek(0)
                    stream.truncate()
refreshPic()