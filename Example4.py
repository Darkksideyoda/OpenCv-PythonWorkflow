#OpenCv Kullanarak Gorseller ile Aritmetik Islemler.

# aritmetik işlemleri göstermek için
# iki görüntünün eklenmesi

import cv2

image1 = cv2.imread('OpenCvDataSets/input1.jpg')#Ilk Gorseli Diskten Okuyoruz
image2 = cv2.imread('OpenCvDataSets/input2.jpg')#Ikinci Gorseli Diskten Okuyoruz


# Bu Noktada cv2.addWeighted Metodundan Biraz Bahsedicek olursak;
#
# Ornek Parametreler üzerinden gierek Aciklayalim
#
# cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
#
# img1: Girilen Ilk Gorsel Tek kanallı, 8 bit veya Ondalikli Degerler Kullanabilirsiniz.
# wt1: Son görüntüye uygulanacak Olan İlk Girilen Gorselin görüntünün ağırlığı
# img2: Girilen Ikinci Gorsel Tek kanallı, 8 bit veya Ondalikli Degerler Kullanabilirsiniz.
# wt2: Son görüntüye uygulanacak Olan Ikinci Girilen Gorselin görüntünün ağırlığı
# gammaValue: Işık ölçümü

weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

#Agirliklari Toplanmis Sonuc Gorselini Ekrana Bastirdigimiz Gui.
cv2.imshow('Weighted Image', weightedSum)

# Bellek Kullanimi Yeniden Tahsis Edilir.
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()