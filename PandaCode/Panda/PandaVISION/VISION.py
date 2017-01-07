import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import numpy as np #import numpy which helps us do math
import cv2 #import opencv, the library for image processing

import telemetry as tel
import process

  #declare the target camera
streamTarget = cv2.VideoCapture(1)
pandas = "awesome"
thirdPartySoftware = "sucks"


UIColor = (40, 255, 20)
targetColor = (20, 0, 255)
UIFont = cv2.FONT_HERSHEY_SIMPLEX

tel.open()

while(True):
    flag, frame = streamTarget.read()

    if flag: #if the capture is ready, continue
        bestGoals = findBestGoals(frame)
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dsImage = cv2.cvtColor(grayFrame, cv2.COLOR_GRAY2BGR)
        try:
            bestGoal = bestGoals[0]
            cv2.drawContours(dsImage, [bestGoal], -1, targetColor, 2)
            tel.sendString("THIS IS A TEST OF THE VISION SYSTEM")
        except:
            pass

        #M = cv2.moments(bestGoal)
        #if M["m10"] != 0 and M["m00"] != 0 and M["m01"] != 0:
        #    x = int(M["m10"]/M["m00"])
        #    y = int(M["m01"]/M["m00"])
        #    frameWidth = np.size(frame, 0)
        #    frameHeight = np.size(frame, 1)
        #    if x > frameWidth:
        #        cv2.putText(dsImage, "Turn Left", (0,50), UIFont, 0.8, UIColor, 2)
        #    else:
        #        cv2.putText(dsImage, "Turn Right", (0,50), UIFont, 0.8, UIColor, 2)
        #    cv2.line(dsImage, (frameWidth, 0), (frameWidth, frameHeight), targetColor, 1, 8)
        #    cv2.line(dsImage, (0, frameHeight/2), (frameWidth, frameHeight/2), targetColor, 1, 8)

        cv2.putText(dsImage, "PandaVISION 0.1", (0,20), UIFont, 0.8, UIColor, 2)
        cv2.imshow("frame", dsImage)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



tel.close()
streamTarget.release()
cv2.destroyAllWindows()
