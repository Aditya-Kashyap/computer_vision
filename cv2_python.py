import numpy as np
import cv2

# Reading a color Image
img = cv2.imread('dog.jpg', 1)
img1 = cv2.imread('dog.jpg', 0)

# cv2.imshow('Image represented here', img)
cv2.imshow('Image represented here', img1)

cv2.imwrite('Dog_BW.png', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
