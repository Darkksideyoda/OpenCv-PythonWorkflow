#Python OpenCv Erosion Islemi



# importing cv2
import cv2

# importing numpy
import numpy as np

# path-Gorselin Bulundugu Dizin
path = r'OpenCvDataSets/input1.jpg'

# Gorseli Diskten Okuyoruz
image = cv2.imread(path)

# Gui Pencere Ismini Veriyoruz.
window_name = 'Image'

# Kernel Olusturma
kernel = np.ones((5, 5), np.uint8)

# Erosion Islemi Icın cv2.erode metodu.
image = cv2.erode(image, kernel)

# Gorseli Gui ile Ekrana Bastirma
cv2.imshow(window_name, image)

#Kullanici Son verene Kadar Ekranda Tutma
cv2.waitKey(0)

#Tum Islemi Bellekten ve ekranda Yok etme.
cv2.destroyAllWindows()

