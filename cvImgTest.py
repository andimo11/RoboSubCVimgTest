import cv2
import numpy as np

image = cv2.imread('/Users/andimop/RoboSub/230.jpg')
pole_img = np.copy(image)
gray = cv2.cvtColor(pole_img, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (3,3),0)
canny = cv2.Canny(blur, 75, 125)

# cv2.imshow('canny', canny)
cv2.imshow('gray', blur)
cv2.waitKey(0)


####tools###
# from PIL import Image
#if using PIL (pillow)
# try:
#     img  = Image.open('/Users/andimop/RoboSub/230.jpg')
#     print('worked1')
# except IOError:
#     pass
