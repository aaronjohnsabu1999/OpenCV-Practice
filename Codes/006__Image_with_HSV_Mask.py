#!/usr/bin/env python
import cv2
import numpy as np

def nilch(pos):
	pass

image01 = cv2.imread('../Sources/Aaron John Sabu.jpg', cv2.IMREAD_COLOR)

cv2.namedWindow   ('Image')
cv2.namedWindow   ('Mask')
cv2.namedWindow   ('Output')

cv2.moveWindow    ('Image',   300, 400)
cv2.moveWindow    ('Mask',    700, 400)
cv2.moveWindow    ('Output', 1100, 400)

cv2.createTrackbar('Lower_Hue', 'Mask', 0, 180, nilch)
cv2.createTrackbar('Upper_Hue', 'Mask', 0, 180, nilch)
cv2.createTrackbar('Lower_Sat', 'Mask', 0, 255, nilch)
cv2.createTrackbar('Upper_Sat', 'Mask', 0, 255, nilch)
cv2.createTrackbar('Lower_Val', 'Mask', 0, 255, nilch)
cv2.createTrackbar('Upper_Val', 'Mask', 0, 255, nilch)

while(True):
	image01 = cv2.imread('./Aaron John Sabu.jpg', cv2.IMREAD_COLOR)
	hsv_01  = cv2.cvtColor(image01, cv2.COLOR_BGR2HSV)

	LH      = cv2.getTrackbarPos('Lower_Hue', 'Mask')
	UH      = cv2.getTrackbarPos('Upper_Hue', 'Mask')
	LS      = cv2.getTrackbarPos('Lower_Sat', 'Mask')
	US      = cv2.getTrackbarPos('Upper_Sat', 'Mask')
	LV      = cv2.getTrackbarPos('Lower_Val', 'Mask')
	UV      = cv2.getTrackbarPos('Upper_Val', 'Mask')
	mask    = cv2.inRange(hsv_01, np.array([LH,LS,LV]), np.array([UH,US,UV]))
	output  = cv2.bitwise_and(image01, image01, mask=mask)

	cv2.imshow('Image', image01)
	cv2.imshow('Mask', mask)
	cv2.imshow('Output', output)

	keyb_inp = cv2.waitKey(10)
	if keyb_inp == 27:
		break

cv2.destroyAllWindows()
