#Girilen sayının istenilen kuvvetini while döngüsü ile alan python programı

sayi = int(input("Sayıyı giriniz :"))
kuvvet = int(input("Kuvveti giriniz :"))

i = 0
carpim = 1
while i < kuvvet:
    carpim *= sayi
    i+=1

print("%d ^ %d = %d" %(sayi,kuvvet,carpim))
