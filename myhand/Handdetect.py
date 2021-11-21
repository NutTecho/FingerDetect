import cv2
import time
import math
import numpy as np
import mediapipe as mp


class handDetection():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands)
        self.mpDraw = mp.solutions.drawing_utils

    
    def findHands(self,frame,draw=True):
        #===== detect hand from frame ========
        imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        # print(result.multi_hand_landmarks)
        if self.result.multi_hand_landmarks:
            for handLms in  self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame,handLms,self.mpHands.HAND_CONNECTIONS)
        return frame
    

    
    def findPosition(self,frame,handNo=0,draw = True):
        # =====draw and get position finger to list =========
        lmList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                    # print(id,lm)
                    h,w,c = frame.shape
                    cx,cy = int(lm.x * w),int(lm.y*h)
                    # print(id,cx,cy)
                    lmList.append([id,cx,cy])
                    # if draw:
                    #     cv2.circle(frame,(cx,cy),10,(0,255,255),cv2.FILLED)

        return lmList