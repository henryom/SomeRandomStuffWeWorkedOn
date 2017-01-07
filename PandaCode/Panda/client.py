import socket
import sys
import pickle
sys.path.append('/usr/local/lib/python2.7/site-packages')

import numpy as np
import cv2

def recvall(count):
    buf = b''
    while count:
        newbuf = s.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

HOST = ""
PORT = 8888
PREFIX = "[CLIENT] > "

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))
except socket.error as error:
    print PREFIX + "connect failed: " + str(error)
    sys.exit()

print PREFIX + "socket connection sucesful"

# try:
#     message = "watch this crash the wifi"
#     s.sendall(message)
# except socket.error as error:
#     print PREFIX + "sendall filed:" + str(error)
#     sys.exit()
# print PREFIX + "message send sucesful, shuting down"
while 1:
    try:
        length = recvall(16)
        data_string = recvall(int(length))
        data = np.fromstring(data_string, dtype="uint8")

        image = cv2.imdecode(data, 1)
        cv2.imshow("CLIENT", image)
    except socket.error as error:
        print PREFIX + "recive failed: " + str(error)
        sys.exit()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
s.close()
