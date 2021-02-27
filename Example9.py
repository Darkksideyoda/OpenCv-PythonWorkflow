
# cv2.copyMakeBorder() metodunu aciklayan python programi

# Gorselin etrafina Border Cizdirmek.

# importing cv2

import cv2



# path Gorselin bulundugu Dizin
path = r'OpenCvDataSets/input1.jpg'



# Gorseli Diskten okuyoruz
image = cv2.imread(path)



# Gui Pencere Adi
window_name = 'Image'



#  cv2.copyMakeBorder() metodu
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT)



cv2.imshow(window_name, image)



cv2.waitKey(0)



#GUI Pencereyi Ekrandan ve Hafizadan Kaldirmak Veya Silmek icin Kullanilir.
cv2.destroyAllWindows()