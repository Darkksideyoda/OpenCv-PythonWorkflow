#Python OpenCv Erosion ve Dilation islemlerine ornek program

import cv2
import numpy as np

# Gorseli diskten okur
img = cv2.imread('OpenCvDataSets/input1.jpg', 0)


# Kernel olarak 5 boyutllu bir matris alinir.
kernel = np.ones((5, 5), np.uint8)


#ilk parametre orjinal gorseldir
#kernel,kıvrımlı görüntünün sahip olduğu matristir
#ucuncu parametre ise ne kadar erode yada dilate edeceginizin
#iterasyon durumudur.

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)#orjinal gorsel basilir
cv2.imshow('Erosion', img_erosion)#erosion gorsel basilir
cv2.imshow('Dilation', img_dilation)#dilate gorsel basilir

cv2.waitKey(0)#kullanicinin Pencereleri kapatana kadar Ekranda Kalmasinin Saglar

cv2.destroyAllWindows()#Tum Pencereleri Bellekten Temizler.