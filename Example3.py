#Python~OpenCv'de Renk Uzayi

import cv2

image = cv2.imread('OpenCvDataSets/RGB_paint.png') #Gorseli Diskten Okuyoruz
B, G, R = cv2.split(image) #Gorseli Split Metoduyla
# Ilgili Kanallara Ayiriyoruz

cv2.imshow("original", image) #Orjinal Gorseli Ekrana Bastir
cv2.waitKey(0)

cv2.imshow("blue", B) #Mavisi Ayrilmis Gorseli Ekrana Bastir
cv2.waitKey(0)

cv2.imshow("Green", G) # Yesili Ayrilmisl Gorseli Ekrana Bastir
cv2.waitKey(0)

cv2.imshow("red", R) # Kirmizisi Ayrilmis Gorseli Ekrana Bastir
cv2.waitKey(0)

cv2.destroyAllWindows()