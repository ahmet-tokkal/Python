#Girilen sayı kadar * dan oluşan içi dolu dörtgen çizen python programı

sayi = int(input("Sayıyı giriniz :"))

for i in range(0,sayi):
    if i==0 or i==sayi-1:
        for j in range(0,sayi):
            print("*",end=" ")
    else:
        print("*",end=" ")
        for j in range(0,sayi-2):
            print(" ",end=" ")
        print("*",end=" ")
    print("\n")
