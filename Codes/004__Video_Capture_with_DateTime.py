#!/usr/bin/env python
import cv2
import numpy as np
import datetime

f_face = cv2.FONT_HERSHEY_SIMPLEX
cam    = cv2.VideoCapture(0)
fcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0
out = cv2.VideoWriter('../Outputs/Camera_02.avi', fcc, fps, (2, 2))
once = True

while(cam.isOpened()):
	datet      = str(datetime.datetime.now())
	ret, frame = cam.read()
	frame_act  = frame
	frame_act  = cv2.flip(frame_act, 1)
	frame_act  = cv2.putText(frame_act, datet, (10,50), f_face, 1, (255,255,0), 2, cv2.LINE_AA)
	if ret == True:
		cv2.imshow('Color', frame_act)
		out.write(frame_act)
	keyb_inp = cv2.waitKey(10) & 0xFF
	if keyb_inp == 27:
		break
cam.release()
out.release()
cv2.destroyAllWindows()
