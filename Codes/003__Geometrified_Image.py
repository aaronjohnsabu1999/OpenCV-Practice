#!/usr/bin/env python
import cv2
import numpy

image01       = cv2.imread('../Sources/Aaron John Sabu.jpg', cv2.IMREAD_COLOR)
height, width = image01.shape[:2]
val           = 5
f_face        = cv2.FONT_HERSHEY_SIMPLEX

image01 = cv2.rectangle(image01,          (val,val),               (width-val, height-val),      (0,0,255),   3)
image01 = cv2.rectangle(image01,          (0,0),                   (val,val),                    (0,0,255),  -1)
image01 = cv2.rectangle(image01,          (width,0),               (width-val, val),             (0,0,255),  -1)
image01 = cv2.rectangle(image01,          (0,height),              (val, height-val),            (0,0,255),  -1)
image01 = cv2.rectangle(image01,          (width,height),          (width-val, height-val),      (0,0,255),  -1)
image01 = cv2.line     (image01,          (val+10, height-val-5),  (width-val-10, height-val-5), (200,0,0),   2)
image01 = cv2.circle   (image01,          (width/2-3,height/2-20), 75,                           (0,255,0),   2)
image01 = cv2.putText  (image01, 'Aaron', (width/2-50, height-val-10), f_face, 1,                (100,100,0), 2)

cv2.imshow('Aaron John Sabu', image01)
keyb_inp = cv2.waitKey(0)
if keyb_inp == 27:
	cv2.destroyAllWindows()
elif keyb_inp == ord('s'):
	cv2.imwrite('../Outputs/Aaron_Geometrified.png', image01)
	cv2.destroyAllWindows()
else:
	print('NA')
