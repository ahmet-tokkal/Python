#Kullanıcıdan alınan pozitif sayının faktoriyelini alan python programı
import sys
sayi = int(input("Pozitif bir sayı giriniz :"))

if sayi < 0:
    print("Lütfen pozitif bir sayı giriniz !")
    sys.exit()
else:
    carpim = 1
    for i in range(1,sayi+1):
        carpim *= i
    print(sayi,"! = ",carpim)
