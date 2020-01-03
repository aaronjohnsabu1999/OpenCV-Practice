#!/usr/bin/env python
import cv2
import numpy as np

def nilch(pos):
	pass

cam = cv2.VideoCapture(0)

cv2.namedWindow('Camera')
cv2.namedWindow('Tracker')
cv2.createTrackbar('Lower_Hue', 'Camera', 0, 180, nilch)
cv2.createTrackbar('Upper_Hue', 'Camera', 0, 180, nilch)
cv2.createTrackbar('Lower_Sat', 'Camera', 0, 255, nilch)
cv2.createTrackbar('Upper_Sat', 'Camera', 0, 255, nilch)
cv2.createTrackbar('Lower_Val', 'Camera', 0, 255, nilch)
cv2.createTrackbar('Upper_Val', 'Camera', 0, 255, nilch)

while(True):
	res, frame = cam.read()

	hsv_01  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	LH = cv2.getTrackbarPos('Lower_Hue', 'Camera')
	UH = cv2.getTrackbarPos('Upper_Hue', 'Camera')
	LS = cv2.getTrackbarPos('Lower_Sat', 'Camera')
	US = cv2.getTrackbarPos('Upper_Sat', 'Camera')
	LV = cv2.getTrackbarPos('Lower_Val', 'Camera')
	UV = cv2.getTrackbarPos('Upper_Val', 'Camera')
	mask    = cv2.inRange(hsv_01, np.array([LH,LS,LV]), np.array([UH,US,UV]))
	output  = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('Camera',  frame)
	cv2.imshow('Tracker', output)

	keyb_inp = cv2.waitKey(5)
	if keyb_inp == 27:
		break

cam.release()
cv2.destroyAllWindows()
