#!/usr/bin/env python
import cv2
import numpy as np

cam = cv2.VideoCapture(0)
fcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0
out = cv2.VideoWriter('../Outputs/Camera_01.avi', fcc, fps, (1280, 960))

while(cam.isOpened()):
	ret, frame = cam.read()
	frame_act  = frame
	frame_act  = np.fliplr(frame_act)
	frame_gray = cv2.cvtColor(frame_act, cv2.COLOR_BGR2GRAY)
	# print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
	# print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
	if ret == True:
		cv2.imshow('Color', frame_act)
		out.write(frame_act)
	keyb_inp = cv2.waitKey(10) & 0xFF
	if keyb_inp == 27:
		break

cam.release()
out.release()
cv2.destroyAllWindows()