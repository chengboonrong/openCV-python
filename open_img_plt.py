import cv2 
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('watch.jpg',1)
gray = cv2.imread('watch.jpg',0)

retval, threshold = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('watchthreshold.png',threshold)
cv2.imwrite('watchgray.png',gray)

cv2.imshow('originak',img)
cv2.imshow('threshold',threshold)


cv2.waitKey(0)
cv2.destroyAllWindows()


