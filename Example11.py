#Python OpenCv Gorseli Olceklendirme


import cv2
import numpy as np

FILE_NAME = 'OpenCvDataSets/input1.jpg'
try:
    # Gorseli diskten Okur
    img = cv2.imread(FILE_NAME)

    # Yatayda Ve dikeydeki Pixel Sayisini Alir.
    (height, width) = img.shape[:2]

    # Interpolasyon metodu ile goruntu boyutunu belirliyoruz.
    # cv2.INTER_AREA parametresi kucultmek icin kullanilirken cv2.INTER_CUBIC
    # buyutmek icin kullanilir.
    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)

    # ilk paramatredeki string degeri gorselin islem gormus ismi olmakla
    # birlikte tekrar diske yazılır.
    cv2.imwrite('result.jpg', res)

except IOError:
    print('Error while reading files !!!')#dosya okunurken Hata ile karsilasilirsa Ekrana bastirilir.