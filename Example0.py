# Gorsel Okumak icin python kodu
import cv2

# diskten Gorsel Okumak Icin
# assagida gosterilen cv2.imread fonksiyonu kullanilir
img = cv2.imread("OpenCvDataSets/starry_night.jpg", cv2.IMREAD_COLOR)

# Ekranda gorseli gostermek icin GUI Arayuzu olustururken cv2.imshow kullanilir
# ilk parametre pencerenin ismi(basligi) olmali ve string bir deger almalidir.
# Ikinci Parametre tanimlanan(img) gorsel array'i olmalidir.
cv2.imshow("Starry Night", img)


# Pencereyi Ekranda tutmak icin cv2.waitKey Metodu Kullanilir
# Cikis Girdisini Tespit Ettiginde Kontrolu bir sonraki satira veya kod Bloguna Birakacaktir.
# İlk Parametre, ekranı milisaniye boyunca tutmak içindir
# Pozitif Bir tamsayi olmalidir. Eger 0 Degeri girilirse Kullanici Kapatana Kadar Pencere Ekranda Kalacaktir.

cv2.waitKey(0)


#GUI Pencereyi Ekrandan ve Hafizadan Kaldirmak Veya Silmek icin Kullanilir.
cv2.destroyAllWindows()





