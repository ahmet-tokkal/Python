#Alınan 3 sayıyı toplayan,çarpan ortalamasını,en küçüğünü ve en büyüğünü bulan c programı.

sayi1=int(input("1.sayiyi giriniz :"))
sayi2=int(input("2.sayiyi giriniz :"))
sayi3=int(input("3.sayiyi giriniz :"))

toplam = sayi1 + sayi2 + sayi3
print("Sayıların Toplamı : ",toplam)
carpim = sayi1 * sayi2 * sayi3
print("Sayıların Çarpımı : ",carpim)
ortalama = toplam / 3
print("Sayiların Ortalaması : ",ortalama)
if sayi1>=sayi2 and sayi1>=sayi3:
    print("En büyük :", sayi1)
    if sayi2>=sayi3:
        print("En küçük :", sayi3)
    else:
        print("En küçük :", sayi2)
elif sayi2>=sayi1 and sayi2>=sayi3:
    print("En büyük :", sayi2)
    if sayi3>=sayi1:
        print("En küçük :", sayi1)
    else:
        print("En küçük :", sayi3)
elif sayi3>=sayi1 and sayi3>=sayi3:
    print("En büyük :", sayi3)
    if sayi2>=sayi1:
        print("En küçük :", sayi1)
    else:
        print("En küçük :", sayi2)
