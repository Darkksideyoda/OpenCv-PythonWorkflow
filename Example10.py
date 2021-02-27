#Python OpenCv GrayScale Ornegi

#Bir onceki GrayScale Orneginden farklı olarak
#cvtColor Metodunu Kullaniyoruz

import cv2

# Gorseli Diskten Okutuyoruz
image = cv2.imread('OpenCvDataSets/input1.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

# cvtColor Metodunu Kullaniyoruz
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)


cv2.destroyAllWindows()