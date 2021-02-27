# Python OpenCv ile Gorselin Kenar tespiti.

# Kenarlari tespit etmek icin cesitli algoritmalar mevcut

# ancak biz bu ornek icin Canny Edge Detection kullanacagiz.

import cv2
import numpy as np

FILE_NAME = 'OpenCvDataSets/input1.jpg'
try:
    # Diskten Gorseli Okur.
    img = cv2.imread(FILE_NAME)

    # Canny Edge Detection algoritmasi.
    edges = cv2.Canny(img, 100, 200)

    # ilk paramatredeki string degeri gorselin islem gormus ismi olmakla
    # birlikte tekrar diske yazılır.
    cv2.imwrite('result.jpg', edges)
except IOError:
    print('Error while reading files !!!')