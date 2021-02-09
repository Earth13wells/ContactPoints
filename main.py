import cv2
import numpy as np
import imutils
from PIL import Image, ImageGrab



# import image
image="/home/gabe/20210208_214301_HDR.jpg"
img = cv2.imread(image)

#Cropping
height,width=img.shape[:2]
start_row,start_col=int(width*0),int(height*0.25+900)
end_row,end_col=int(width*1),int(height*0.5+900)
cropped=img[start_row:end_row,start_col:end_col]



#location of colour
color = ((242, 243, 244))
pixels = np.argwhere(cropped == color)
print(pixels)


# convert to hsv
hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)

#Define colour ranges
lower_range_dial = np.array([0,0,50])
upper_range_dial = np.array([400,100,100])

mask_dial = cv2.inRange(hsv, lower_range_dial, upper_range_dial)

lower_range_crow = np.array([0,0,50])
upper_range_crow = np.array([400,100,100])

mask_crow = cv2.inRange(hsv, lower_range_crow, upper_range_crow)

out_img = cv2.add(mask_dial,mask_crow)
image[0:rows, 0:cols ] = out_img

#cv2.imshow('image', img)
cv2.imshow('mask', mask)
cv2.imshow('out', out_img)

while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()
