
# importing cv2
import cv2

# path-Gorsel Yolu
path = r'OpenCvDataSets/starry_night.jpg'

# cv2.imread() Gorseli Okuyoruz
# Gorseli GrayScale Modda Okumak Icin 0 Parametresi Veriyoruz.
img = cv2.imread(path, 0)


# Ekrana Bastiriyoruz
cv2.imshow('Starry Night GrayScale', img)

# Biz Kapatana Kadar Ekranda Tutuyoruz
cv2.waitKey(0)

#GUI Pencereyi Ekrandan ve Hafizadan Kaldirmak Veya Silmek icin Kullanilir.
cv2.destroyAllWindows()

