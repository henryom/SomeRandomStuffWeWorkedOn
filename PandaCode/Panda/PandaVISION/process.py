import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2 #import opencv, the library for image processing
import numpy as np #import numpy which helps us do math

rangeMin = np.array([30,0,250])
rangeMax = np.array([100,30,255])

aspctRtioMin = 0
aspctRtioMax = 4

areaperMin = 0
areaperMax = 30

def goalSortKey(goal):
    x,y,w,h = cv2.boundingRect(goal)
    perm = cv2.arcLength(goal, True)
    return w*h*perm

def findBestGoals(frame):
    bgr = frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    b = cv2.inRange(hsv, rangeMin, rangeMax)
    im2, contours, hierarchy = cv2.findContours(b,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    goals = []

    for contour in contours: #I LOVE PYTHON!!! MY FAVORITE LOOP!!!  This loop removes unwanted contours

        x,y,w,h = cv2.boundingRect(contour)
        apct = w/h

        area = cv2.contourArea(contour)
        perm = cv2.arcLength(contour, True)

        areaperm = 0
        if area != 0 and perm != 0:
            areaperm = area/perm

        if area > 1000:
            if apct > aspctRtioMin and apct < aspctRtioMax:
                if areaperm > areaperMin and areaperm < areaperMax:
                    goals.append(contour)

    goals = sorted(goals, key=goalSortKey, reverse=True)

    if not goals:
        return None
    else:
        return goals
