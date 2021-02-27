# cv2.imwrite() metodunu Aciklamak Icin Yazilan Python Programi

# importing cv2
import cv2

# importing os module
import os




# Gorsel path(Dizin)
image_path = r'OpenCvDataSets/starry_night.jpg'

# Image directory(Depolanacagi Dizin)
directory = r'C:\Users\Bahtiyar\Desktop\Desktop'


# method Gorseli Okumak Icin  cv2.imread()

img = cv2.imread(image_path)

# Mevcut dizini belirtilen dizinle degistirir.
os.chdir(directory)

# Kayit Yaptiginiz Dizindeki Dosyalari ve Klasorleri listeler.
# in 'C:\Users\Bahtiyar\Desktop\Desktop'
print("Before saving image:")
print(os.listdir(directory))

# Kaydedilen Dosyanin Adi.
filename = 'savedImage.jpg'

# Gorseli Kaydetmek Icin cv2.imwrite() method Kullanilir
cv2.imwrite(filename, img)

# Kayit Yaptiktan Sonra Tekrar Dizindeki Dosyalari ve Klasorleri listeler.
print("After saving image:")
print(os.listdir(directory))


print('Successfully saved')#Kayit Basarili.