import socket
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy
import cv2


HOST = "localhost"
PORT = 5001
conn, addr = None

def open:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(True)
    conn, addr = s.accept()

def sendString(msg):
    conn.send(msg.ljust(16))

def close:
    s.close()
