#!/usr/bin/env python
import cv2
import numpy as np

def nilch(pos):
	pos = pos

image01       = cv2.imread('../Sources/Aaron John Sabu.jpg', cv2.IMREAD_COLOR)
height, width = image01.shape[:2]
val           = 5
f_face        = cv2.FONT_HERSHEY_SIMPLEX

cv2.namedWindow   ('Image')
cv2.createTrackbar('X',         'Image', 0, height-1, nilch)
cv2.createTrackbar('Y',         'Image', 0, width-1,  nilch)
cv2.createTrackbar('B',         'Image', 0, 255,      nilch)
cv2.createTrackbar('G',         'Image', 0, 255,      nilch)
cv2.createTrackbar('R',         'Image', 0, 255,      nilch)
cv2.createTrackbar('Size',      'Image', 0, 10,       nilch)
cv2.createTrackbar('Thickness', 'Image', 0, 10,       nilch)

cv2.setTrackbarPos('X',         'Image', 0)
cv2.setTrackbarPos('Y',         'Image', 205)
cv2.setTrackbarPos('B',         'Image', 165)
cv2.setTrackbarPos('G',         'Image', 65)
cv2.setTrackbarPos('R',         'Image', 110)
cv2.setTrackbarPos('Size',      'Image', 01)
cv2.setTrackbarPos('Thickness', 'Image', 02)

while(True):
	image01 = cv2.imread('../Sources/Aaron John Sabu.jpg', cv2.IMREAD_COLOR)
	X       = cv2.getTrackbarPos('X',         'Image')
	Y       = cv2.getTrackbarPos('Y',         'Image')
	B       = cv2.getTrackbarPos('B',         'Image')
	G       = cv2.getTrackbarPos('G',         'Image')
	R       = cv2.getTrackbarPos('R',         'Image')
	S       = cv2.getTrackbarPos('Size',      'Image')
	T       = cv2.getTrackbarPos('Thickness', 'Image')
	image01 = cv2.putText(image01, 'Aaron', (X, Y), f_face, S, (B, G, R), T)
	cv2.imshow('Image', image01)
	keyb_inp = cv2.waitKey(10)
	if keyb_inp == 27:
		break

cv2.destroyAllWindows()