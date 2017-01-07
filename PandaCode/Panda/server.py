import socket
import sys
import pickle
sys.path.append('/usr/local/lib/python2.7/site-packages')

import numpy as np
import cv2

HOST = ""
PORT = 8888
PREFIX = "[SERVER] > "

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
streamTarget = cv2.VideoCapture(0)

try:
    s.bind((HOST, PORT))
except socket.error as error:
    print PREFIX + "bind failed: " + str(error)
    sys.exit()

print PREFIX + "socket bind sucesful!"

s.listen(10)
print PREFIX + "listening!"

while 1:
    conn, addr = s.accept()
    print PREFIX + "connected with " + addr[0] + ":" + str(addr[1])
    # try:
    #     data = conn.recv(1024)
    #     print PREFIX + "recived data:" + data
    # except socket.error as error:
    #     print PREFIX + "recive failed:" + str(error)
    #     sys.exit()
    try:
        #message = "watch this crash the wifi"
        while 1:
            flag, frame = streamTarget.read()

            encodeArgs = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
            result, imgencode = cv2.imencode(".jpg", frame, encodeArgs)
            data = np.array(imgencode)
            stringData = data.tostring()

            conn.send(str(len(stringData)).ljust(16))
            conn.send(stringData)

        #cv2.putText(frame, "PandaVISION 0.1", (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (40, 255, 20), 1)
        #pickled_image = pickle.dumps(frame)

        #array = ["item1", "itemtwo", "itemthwee"]
        #pickled_array = pickle.dumps(array)
        #conn.sendall(pickled_image)
    except socket.error as error:
        print PREFIX + "sendall filed:" + str(error)
        sys.exit()
s.close()
