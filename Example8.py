
#OpenCv Gorselleri Blurlama(Bulaniklastirma)

# Bu Noktada Koda Gecmeden Once Bir oneride Bulunmak Istiyorum
# Filtreleme metodlarinin Matematiksel modellemeleri Kutuphane ile Hazir Geldiginden
# Isin Ozunu anlamak adina oncelikle Basit bir literatur arastirmasi yapmakta fayda var
# ornegin gauss filtreleme metodunun calisma prensibi vs.

import cv2
import numpy as np

image = cv2.imread('OpenCvDataSets/input1.jpg')#Dizinden Gorseli Okuyorum.

cv2.imshow('Original Image', image)#Orjinal Gorseli Ekrana Bastır.
cv2.waitKey(0)#Ekranda Kullanici Kapatana Kadar Bastirir.

# Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

# Median Blur
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

# Bilateral Blur
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()