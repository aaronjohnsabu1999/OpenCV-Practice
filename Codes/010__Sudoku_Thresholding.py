#!/usr/bin/env python
import cv2
import numpy as np

def nilch(pos):
	pass

cv2.namedWindow('Image')
cv2.namedWindow('Adaptive_Mean_Threshold')
cv2.namedWindow('Adaptive_Gaussian_Threshold')

cv2.moveWindow('Image',                        500, 400)
cv2.moveWindow('Adaptive_Mean_Threshold',     1000, 200)
cv2.moveWindow('Adaptive_Gaussian_Threshold', 1000, 600)

image01 = cv2.imread('../Sources/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
cv2.createTrackbar('Constant',   'Image', 0,  5, nilch)
cv2.createTrackbar('Block_Size', 'Image', 0, 25, nilch)

cv2.setTrackbarPos('Constant',   'Image', 2)
cv2.setTrackbarPos('Block_Size', 'Image', 5)

while(True):
	cv2.imshow('Image', image01)
	C    = cv2.getTrackbarPos('Constant',   'Image')
	Size = cv2.getTrackbarPos('Block_Size', 'Image')
	if (Size % 2 == 0):
		Size = Size + 1
		cv2.setTrackbarPos('Block_Size', 'Image', Size)
	if (Size < 3):
		Size = 3
		cv2.setTrackbarPos('Block_Size', 'Image', Size)
	thr01    = cv2.adaptiveThreshold(image01, 255, cv2.ADAPTIVE_THRESH_MEAN_C,     cv2.THRESH_BINARY, Size, C)
	thr02    = cv2.adaptiveThreshold(image01, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, Size, C)
	cv2.imshow('Adaptive_Mean_Threshold',     thr01)
	cv2.imshow('Adaptive_Gaussian_Threshold', thr02)
	keyb_inp = cv2.waitKey(1)
	if keyb_inp == 27:
		break

cv2.destroyAllWindows()
