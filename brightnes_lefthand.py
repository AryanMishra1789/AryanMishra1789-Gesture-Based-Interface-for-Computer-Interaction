import cv2
import numpy as np
import mediapipe as mp
# import time
# import os
from math import hypot
import screen_brightness_control as sbc

def Brightness(frame,frameRGB,results,Draw,mphands,hands):##left hand
        landmarkList=[]
        if results.multi_hand_landmarks:
            for handlm in results.multi_hand_landmarks:
                for id, lm in enumerate(handlm.landmark):
                    h, w, c = frame.shape
                    x,y=int(lm.x*w),int(lm.y*h)
                    landmarkList.append([id,x,y])
                Draw.draw_landmarks(frame,
                                    handlm,
                                    mphands.HAND_CONNECTIONS)
        if landmarkList !=[]:
            x_1,y_1=landmarkList[4][1],landmarkList[4][2]
            x_2,y_2=landmarkList[8][1],landmarkList[8][2]
            cv2.circle(frame,(x_1,y_1),5,(0,255,0),
                       cv2.FILLED)
            cv2.circle(frame,(x_2,y_2),5,(0,255,0),
                       cv2.FILLED)
            cv2.line(frame,(x_1,y_1),(x_2,y_2),(255,0,0),3)
            L=hypot(x_2-x_1,y_2-y_1)
            b_level=np.interp(L,[15,220],[15,100])
            sbc.set_brightness(int(b_level))
        cv2.imshow('img',frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
# cap.release()
# cv2.destroyAllWindows()
