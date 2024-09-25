import cv2
import numpy as np

# Load the image
img2 = cv2.imread("messi5.jpg")

# Resize img2 to match the dimensions of img1
img2 = cv2.resize(img2, (500, 250))

# Now you can perform bitwise operations
img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
#bitAnd = cv2.bitwise_and(img2 , img1)
#bitor = cv2.bitwise_or(img2, img1)
#bitXor = cv2.bitwise_xor(img1 , img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
#cv2.imshow('bitAnd' , bitAnd)
#cv2.imshow('bitor', bitor)
#cv2.imshow('bitAnd' , bitXor)
cv2.imshow('bitAnd', bitNot1)
cv2.imshow('bitAnd',bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()
