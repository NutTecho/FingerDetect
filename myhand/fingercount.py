import cv2
import time
import math
import os
import numpy as np
import mediapipe as mp
from Handdetect import handDetection


def setimage():
    folderPath = ""
    imglist = os.listdir(folderPath)
    overlaylist = []
    # for impath in imglist:
        # impath = cv2.imread(f'{folderPath}'/)



def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    tipID = [4,8,12,16,20]
    detector = handDetection()

    while True:
        ret,frame = cap.read()
        frame = detector.findHands(frame)
        lmlist = detector.findPosition(frame)

        if len(lmlist) != 0:
            finger = []

            # thumb left hand only
            if lmlist[tipID[0]][1] < lmlist[tipID[0]-1][1]:
                finger.append(1)
            else:
                finger.append(0)
                
            # 4 finger left hand only
            for id in range(1,5):
                if lmlist[tipID[id]][2] < lmlist[tipID[id]-2][2]:
                    finger.append(1)
                else:
                    finger.append(0)
            print(finger)

            fingercount = finger.count(1)
            cv2.rectangle(frame,(20,225),(170,425),(0,0,0),cv2.FILLED)
            cv2.putText(frame,str(int(fingercount)),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(0,0,255),8)



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