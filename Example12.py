#Python OpenCv ile Gorseli Rotate(dondurme) etme islemi.

import cv2
import numpy as np

FILE_NAME = 'OpenCvDataSets/input1.jpg'

try:

    img = cv2.imread(FILE_NAME)

    # Yatayda Ve dikeydeki Pixel Sayisini Alir.
    (rows, cols) = img.shape[:2]


    # getRotationMatrix2D, donusum icin gerekli bir matris olusturur
    # Ölçeklendirmeden 45 derece merkeze w.r.t rotasyon için matris istiyoruz.
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    res = cv2.warpAffine(img, M, (cols, rows))

    # ilk paramatredeki string degeri gorselin islem gormus ismi olmakla
    # birlikte tekrar diske yazılır.
    cv2.imwrite('result.jpg', res)
except IOError:
    print('Error while reading files !!!') #dosya okunurken Hata ile karsilasilirsa Ekrana bastirilir.