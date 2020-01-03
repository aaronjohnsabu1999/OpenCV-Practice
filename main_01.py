#!/usr/bin/env python
import cv2
import numpy

image01 = cv2.imread('/home/aaronjs/Documents/Pictures/Aaron John Sabu.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Aaron John Sabu', image01)
keyb_inp = cv2.waitKey(0)
if keyb_inp == 27:
	cv2.destroyAllWindows()
elif keyb_inp == ord('s'):
	cv2.imwrite('./Aaron_Grayscale.png', image01)
	cv2.destroyAllWindows()
else:
	print('NA')
