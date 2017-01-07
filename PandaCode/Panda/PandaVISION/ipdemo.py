import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import numpy as np
import cv2
import urllib

ipcamaddr = "http://10.29.15.87/mjpg/video.mjpg"



#cap = cv2.VideoCapture(ipcamaddr)
#while True:
#    flag, frame = cap.read()
#    cv2.imshow('Video', frame)
#    if cv2.waitKey(1) == 27:
#        exit(0)

stream = urllib.urlopen(ipcamaddr)
bytes=''

while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
        cv2.imshow("i", i)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#if capture.open(ipcamaddr):
#    print "Capture failed"

#while(True):
#    frame = capture.read()
#        if flag:
#            cv2.imshow("frame", frame)
#
#streamTarget.release()
#cv2.destroyAllWindows()
