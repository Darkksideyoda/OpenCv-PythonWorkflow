
# Python OpenCv Translating islemi
# Translating derken yapmak istenen
# Referans Cerceve dogrultusunda gorseli shift (Kaydirma) etme.

import cv2
import numpy as np

FILE_NAME = 'OpenCvDataSets/input1.jpg'

#translation Matrisi olusturuyoruz.
#Kaydirma (x,y) olmak uzere Matrix;
# M = [1 0 x]
#     [0 1 y]
# Kaydirma degerimiz (100, 50) olsun.

M = np.float32([[1, 0, 100], [0, 1, 50]])

try:

    # Gorseli diskten Okur
    img = cv2.imread(FILE_NAME)

    # Yatayda Ve dikeydeki Pixel Sayisini Alir.
    (rows, cols) = img.shape[:2]

    # warpAffine does appropriate shifting given the
    # translation matrix.

    # warpAffine olusturulan Translation Matrix'e gore
    # Kaydirma islemini yapar.
    res = cv2.warpAffine(img, M, (cols, rows))

    # ilk paramatredeki string degeri gorselin islem gormus ismi olmakla
    # birlikte tekrar diske yazılır.
    cv2.imwrite('result.jpg', res)

except IOError:
    print('Error while reading files !!!') #dosya okunurken Hata ile karsilasilirsa Ekrana bastirilir.