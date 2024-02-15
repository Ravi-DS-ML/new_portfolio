import cv2

img = cv2.imread('./assets/img/18141.jpg')

img = cv2.resize(img, (1920, 1280))

cv2.imwrite('./assets/img/back_new.jpg', img)