import cv2
import numpy as np
from matplotlib import pyplot as plt

def nilch(pos):
	pass

image01 = cv2.imread('../Sources/Aaron John Sabu.jpg')
# image01 = cv2.cvtColor(image01, cv2.COLOR_BGR2RGB)

cv2.namedWindow   ('Image')
cv2.namedWindow   ('2DConv')
cv2.namedWindow   ('Blur')
cv2.namedWindow   ('Gauss')
cv2.namedWindow   ('Median')
cv2.namedWindow   ('Bilat')

cv2.moveWindow    ('Image',    50, 100)
cv2.moveWindow    ('2DConv',  425, 100)
cv2.moveWindow    ('Blur',    800, 100)
cv2.moveWindow    ('Gauss',  1125, 100)
cv2.moveWindow    ('Median',   425, 400)
cv2.moveWindow    ('Bilat',    800, 400)

cv2.createTrackbar('Dilation Size', 'Image', 1, 120, nilch)
cv2.setTrackbarPos('Dilation Size', 'Image', 5)

while(True):
	kernel_size  = max(cv2.getTrackbarPos('Dilation Size', 'Image'), 1)
	kernel       = np.ones((kernel_size,kernel_size), np.uint8)/float(kernel_size**2)
	gkernel_size = max(cv2.getTrackbarPos('Dilation Size', 'Image'), 1)*2 - 1
	
	image01 = cv2.imread('../Sources/Aaron John Sabu.jpg')
	dst     = cv2.filter2D       (image01, -1, kernel)
	blur    = cv2.blur           (image01, ( kernel_size,  kernel_size))
	gauss   = cv2.GaussianBlur   (image01, (gkernel_size, gkernel_size), 0)
	median  = cv2.medianBlur     (image01,  gkernel_size)
	bilat   = cv2.bilateralFilter(image01,   kernel_size, 75, 75)
	
	cv2.imshow('Image',  image01)
	cv2.imshow('2DConv', dst)
	cv2.imshow('Blur',   blur)
	cv2.imshow('Gauss',  gauss)
	cv2.imshow('Median', median)
	cv2.imshow('Bilat',  bilat)

	keyb_inp = cv2.waitKey(10)
	if keyb_inp == 27:
		break
		cv2.destroyAllWindows()
	elif keyb_inp == ord('d'):
		cv2.imwrite('../Outputs/Aaron_2DConv_'         +str(kernel_size)+'.png', dst)
	elif keyb_inp == ord('b'):
		cv2.imwrite('../Outputs/Aaron_Blur_'           +str(kernel_size)+'.png', blur)
	elif keyb_inp == ord('g'):
		cv2.imwrite('../Outputs/Aaron_GaussBlur_'      +str(kernel_size)+'.png', gauss)
	elif keyb_inp == ord('m'):
		cv2.imwrite('../Outputs/Aaron_Median_'         +str(kernel_size)+'.png', median)
	elif keyb_inp == ord('l'):
		cv2.imwrite('../Outputs/Aaron_BilateralFilter_'+str(kernel_size)+'.png', bilat)

cv2.destroyAllWindows()