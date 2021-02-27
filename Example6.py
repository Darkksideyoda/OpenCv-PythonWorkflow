
#OpenCv Gorseli Yeniden Boyutlandirma Ornegi.

import os
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


# cv2.INTER_AREA: Bu, bir görüntüyü küçültmemiz gerektiğinde kullanılır.
# cv2.INTER_CUBIC: yavaş ama daha etkilidir.
# cv2.INTER_LINEAR: Eğer yakınlaştırma gerekiyorsa kullanılır.OpenCV'deki varsayılan enterpolasyon tekniğidir.
# Parametreleri Dokumandan Inceleyebilirsiniz.


image = cv2.imread("OpenCvDataSets/RGB_paint.png", 1)#Gorseli Okuyoruz


directory = r'C:\Users\Bahtiyar\Desktop\Desktop' # Kayit Dizinini Belirtiyorum
os.chdir(directory)#Mevcut dizini belirtilen dizinle degistirir.

half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)#cv.resize Metodu Gorseli Yeniden Boyutlandirmamizi Sagliyor.
bigger = cv2.resize(image, (1050, 1610))

stretch_near = cv2.resize(image, (780, 540),
                          interpolation=cv2.INTER_NEAREST)

filename = 'savedImage.jpg'#Kaydedilecek Gorselin Adi.

cv2.imwrite(filename, bigger)#Gorselin Kayedi.


#plot Komutlari
Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [image, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()