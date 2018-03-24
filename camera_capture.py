import numpy as np
import cv2

cap = cv2.VideoCapture(0) # allow camara to capture image (input)

while True:
	ret, frame = cap.read()
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # gray images

	retval, threshold = cv2.threshold(gray_frame, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	cv2.imshow('frame',frame) # show frames in color
	cv2.imshow('gray',threshold) # show frames in gray

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()