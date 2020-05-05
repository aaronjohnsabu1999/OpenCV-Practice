#!/usr/bin/env python
import cv2
import numpy as np
import copy
from matplotlib import pyplot as plt

def nilch(pos):
	pass

cv2.namedWindow   ('Image')
cv2.namedWindow   ('Mask')
cv2.namedWindow   ('Dilation')
cv2.namedWindow   ('Erosion')
cv2.namedWindow   ('Opening')
cv2.namedWindow   ('Closing')
cv2.namedWindow   ('Gradient')
cv2.namedWindow   ('TopHat')
cv2.namedWindow   ('Dil-Ero')
cv2.namedWindow   ('Norm')

cv2.moveWindow    ('Image',      50, 100)
cv2.moveWindow    ('Mask',      425, 100)
cv2.moveWindow    ('Dilation',  800, 100)
cv2.moveWindow    ('Erosion',  1125, 100)
cv2.moveWindow    ('Opening',    50, 400)
cv2.moveWindow    ('Closing',   425, 400)
cv2.moveWindow    ('Gradient',  800, 400)
cv2.moveWindow    ('TopHat',   1125, 400)
cv2.moveWindow    ('Dil-Ero',   425, 700)
cv2.moveWindow    ('Norm',      800, 700)

cv2.createTrackbar('Dilation Size', 'Mask', 0, 120, nilch)

while(True):
	kernel_size = cv2.getTrackbarPos('Dilation Size', 'Mask')

	image01     = cv2.imread('../Sources/Aaron John Sabu.jpg', cv2.IMREAD_GRAYSCALE)
	_, mask     = cv2.threshold(image01, 220, 255, cv2.THRESH_BINARY_INV)
	kernel      = np.ones((kernel_size,kernel_size), np.uint8)
	dilation    = cv2.dilate(mask, kernel, iterations=1)
	erosion     = cv2.erode (mask, kernel, iterations=1)
	opening     = cv2.morphologyEx(mask, cv2.MORPH_OPEN,     kernel)
	closing     = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,    kernel)
	gradient    = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
	tophat      = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT,   kernel)

	dil_ero     = dilation - erosion
	# norm will set a cell to LOW if the majority of cells around it are LOW, else the cell will be HIGH
	norm        = copy.deepcopy(mask)
	for row in range(len(mask)):
		for cell in range(len(mask[row])):
			val = [-1 for i in range(8)]
			# for i in range(8):
			# 	try:
			# 		val[i] = mask[row+((i-4)%3)][cell+int((i-4)/3)]
			# 	except Exception:
			# 		val[i] = 1
			try:
				val[0] = mask[row-1][cell-1]
			except Exception:
				val[0] = 1
			try:
				val[1] = mask[row-1][cell]
			except Exception:
				val[1] = 1
			try:
				val[2] = mask[row-1][cell+1]
			except Exception:
				val[2] = 1
			try:
				val[3] = mask[row][cell+1]
			except Exception:
				val[3] = 1
			try:
				val[4] = mask[row+1][cell+1]
			except Exception:
				val[4] = 1
			try:
				val[5] = mask[row+1][cell]
			except Exception:
				val[5] = 1
			try:
				val[6] = mask[row+1][cell-1]
			except Exception:
				val[6] = 1
			try:
				val[7] = mask[row][cell-1]
			except Exception:
				val[7] = 1
			a = val.count(0)
			b = val.count(255)
			if (a > b):
				norm[row][cell] = 0
			else:
				norm[row][cell] = 255
			
	cv2.imshow('Image',    image01)
	cv2.imshow('Mask',     mask)
	cv2.imshow('Dilation', dilation)
	cv2.imshow('Erosion',  erosion)
	cv2.imshow('Opening',  opening)
	cv2.imshow('Closing',  closing)
	cv2.imshow('Gradient', gradient)
	cv2.imshow('TopHat',   tophat)
	cv2.imshow('Dil-Ero',  dil_ero)
	cv2.imshow('Norm',     norm)
	
	keyb_inp = cv2.waitKey(10)
	if keyb_inp == 27:
		break
		cv2.destroyAllWindows()
	elif keyb_inp == ord('m'):
		cv2.imwrite('../Outputs/Aaron_Masked.png', mask)
	elif keyb_inp == ord('d'):
		cv2.imwrite('../Outputs/Aaron_Dilated_' +str(kernel_size)+'.png', dilation)
	elif keyb_inp == ord('e'):
		cv2.imwrite('../Outputs/Aaron_Eroded_'  +str(kernel_size)+'.png', erosion)
	elif keyb_inp == ord('o'):
		cv2.imwrite('../Outputs/Aaron_Opening_' +str(kernel_size)+'.png', opening)
	elif keyb_inp == ord('c'):
		cv2.imwrite('../Outputs/Aaron_Closing_' +str(kernel_size)+'.png', closing)
	elif keyb_inp == ord('g'):
		cv2.imwrite('../Outputs/Aaron_Gradient_'+str(kernel_size)+'.png', gradient)
	elif keyb_inp == ord('t'):
		cv2.imwrite('../Outputs/Aaron_TopHat_'+  str(kernel_size)+'.png', tophat)
	elif keyb_inp == ord('f'):
		cv2.imwrite('../Outputs/Aaron_Dil-Ero_' +str(kernel_size)+'.png', dil_ero)
	elif keyb_inp == ord('n'):
		cv2.imwrite('../Outputs/Aaron_Norm.png', norm)

cv2.destroyAllWindows()