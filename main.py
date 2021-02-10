import cv2
import time
import numpy as np
import imutils
from PIL import Image, ImageGrab
#Guvcview
while True:
    cap = cv2.VideoCapture(0)

    while True: # capture frame
        ret, frame = cap.read()
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord(' '): # wait until space key
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    #Cropping crop image
    #height,width=frame.shape[:2]
    #start_row,start_col=int(0),int(0)
    #end_row,end_col=int(width),int(height)
    #cropped=frame[start_row:end_row,start_col:end_col]

    # convert to hsv from rgb
    hsved = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Define colour ranges
    lower_range_dial = np.array([0,40,0])
    upper_range_dial = np.array([100,50,200]) # change this to colour of dial marks

    mask_dial = cv2.inRange(hsved, lower_range_dial, upper_range_dial)
    cv2.imshow('mask_dial', mask_dial)

    lower_range_crow = np.array([0,210,0])
    upper_range_crow = np.array([400,220,400]) # change this to colour of crows foot

    mask_crow = cv2.inRange(hsved, lower_range_crow, upper_range_crow)
    #location of crowsfoot
    #print(np.average(mask_crow, axis=1))
    for i in range(1):
        #print(mask_crow[1000:1000])
        a = (mask_crow.mean(axis=0))
        c = [i for i, j in enumerate(a) if j == max(a)]
        b = (mask_crow.mean(axis=1))
        d = [i for i, k in enumerate(b) if k == max(b)]
        print(np.average(c))
        print(np.average(d))
    cv2.circle(mask_crow,(int(np.average(c)),int(np.average(d))), 5, (150,55,55), -1)
    cv2.imshow('mask_crow', mask_crow)
    # combine masks
    comb_img = mask_crow | mask_dial
    cv2.imshow('combined', comb_img[:])

    time.sleep(1)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(0)
    time.sleep(10)
