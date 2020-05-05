#!/usr/bin/env python
import cv2
import numpy as np
import matplotlib.pyplot as plt

def nilch(pos):
	pass

image01 = cv2.imread('../Sources/Aaron John Sabu.jpg', cv2.IMREAD_GRAYSCALE)
image01 = cv2.cvtColor(image01, cv2.COLOR_BGR2RGB)

_, thr01 = cv2.threshold(image01, 50,  255, cv2.THRESH_BINARY)
_, thr02 = cv2.threshold(image01, 200, 255, cv2.THRESH_BINARY_INV)
_, thr03 = cv2.threshold(image01, 127, 255, cv2.THRESH_TRUNC)
_, thr04 = cv2.threshold(image01, 127, 255, cv2.THRESH_TOZERO)
_, thr05 = cv2.threshold(image01, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [image01, thr01, thr02, thr03, thr04, thr05]

for i in xrange(6):
	plt.subplot(2, 3, i+1)
	plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])
plt.show()
