import cv2
import time
import os
import math
import numpy as np
import mediapipe as mp
from Handdetect import handDetection

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetection()
    while True:

        ret,frame = cap.read()
        frame = detector.findHands(frame)
        lmlist = detector.findPosition(frame)
        if len(lmlist) != 0:
            # print(lmlist[4],lmlist[8])

            x1,y1 = lmlist[4][1],lmlist[4][2]
            x2,y2 = lmlist[8][1],lmlist[8][2]
            cx,cy = (x1+x2) // 2, (y1+y2) // 2

            cv2.circle(frame,(x1,y1),10,(0,255,255),cv2.FILLED)
            cv2.circle(frame,(x2,y2),10,(0,255,255),cv2.FILLED)

            cv2.line(frame,(x1,y1),(x2,y2),(0,255,255),3)
            cv2.circle(frame,(cx,cy),10,(0,255,255),cv2.FILLED)

            length = math.hypot(x2-x1,y2-y1)
            # print(length)

            vol = np.interp(length,[50,300],[400,150])
            volPer = np.interp(length,[50,300],[0,100])

        cv2.rectangle(frame,(50,150),(85,400),(255,0,0),3)
        cv2.rectangle(frame,(50,int(vol)),(85,400),(255,0,0),cv2.FILLED)
        cv2.putText(frame,f'{int(volPer)}%',(40,450),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)

        #=== frame rate monitor========
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),2)
        #==============================

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
    

