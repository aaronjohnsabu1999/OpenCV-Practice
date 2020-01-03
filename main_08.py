#!/usr/bin/env python
import cv2
import numpy as np

def nilch(pos):
	pass

cv2.namedWindow('Image')
image01 = cv2.imread('/home/aaronjs/Documents/Pictures/Aaron John Sabu.jpg', cv2.IMREAD_GRAYSCALE)
cv2.createTrackbar('Threshold', 'Image', 0, 255, nilch)

while(True):
	cv2.imshow('Image', image01)
	Thresh = cv2.getTrackbarPos('Threshold', 'Image')
	_, thr01 = cv2.threshold(image01, Thresh, 255, cv2.THRESH_BINARY)
	_, thr02 = cv2.threshold(image01, Thresh, 255, cv2.THRESH_BINARY_INV)
	_, thr03 = cv2.threshold(image01, Thresh, 255, cv2.THRESH_TRUNC)
	_, thr04 = cv2.threshold(image01, Thresh, 255, cv2.THRESH_TOZERO)
	_, thr05 = cv2.threshold(image01, Thresh, 255, cv2.THRESH_TOZERO_INV)
	cv2.imshow('Binary_Threshold',      thr01)
	cv2.imshow('Binary_Inv_Threshold',  thr02)
	cv2.imshow('Trunc_Threshold',       thr03)
	cv2.imshow('To_Zero_Threshold',     thr04)
	cv2.imshow('To_Zero_Inv_Threshold', thr05)
	keyb_inp = cv2.waitKey(10)
	if keyb_inp == 27:
		break

cv2.destroyAllWindows()
