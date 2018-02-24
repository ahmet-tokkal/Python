"""
Oyuncu iki zarı aynı anda atar. iki zarında altı yüzü vardır.
Bu yüzlerde 1,2,3,4,5 ve 6 adet nokta bulunur.
Zarlar durduktan sonra her iki zarında üste gelen yüzleri toplanır.
Eğer toplam ilk atışta 7 ya da 11 ise oyuncu kazanır.
Eğer toplam ilk atışta 2,3 ya da 12 gelirse (buna barbut denir) oyuncu kaybeder.
Eğer ilk atışta toplam 4,5,6,8,9,10 ise bu toplam oyuncunun sayısı haline gelir.
Kazanmak için oyuncu sayısını bulana kadar zarları atmaya devam eder.
Zarları atmaya devam ederken kendi sayısı yerine 7 atarsa kaybeder.

"""

import random
def zarAt():
    zar1 = random.randint(1,7)
    zar2 = random.randint(1,7)
    print("1.Zar : ",zar1)
    print("2.Zar : ",zar2)
    toplam = zar1 + zar2
    print("Toplam : ",toplam)
    return toplam

toplam = zarAt()
durum = 0
if(toplam == 7 or toplam == 11):
    print("Tebrikler kazandın!!!")
    durum = 1
elif(toplam == 2 or toplam == 3 or toplam == 12):
    print("Maalesef Kaybettiniz!!!")
    durum = 2
else:
    oyuncuPuani = toplam
    print("Kazanman için atman gereken  zar : ",oyuncuPuani)

while durum == 0:
    toplam = zarAt()
    if toplam == oyuncuPuani:
        print("Tebrikler kazandın!!!")
        durum = 1
    elif toplam == 7:
        print("Maalesef Kaybettiniz!!!")
        durum = 2
        
    
