#Girilen sayı kadar * dan oluşan içi dolu dörtgen çizen C programı

sayi = int(input("Sayıyı giriniz :"))
for i in range(0,sayi):
    for j in range(0,sayi):
        print("*",end=" ")
    print("\n")
           
