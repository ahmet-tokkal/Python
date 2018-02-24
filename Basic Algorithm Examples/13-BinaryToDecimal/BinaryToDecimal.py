#Girilen ikilim sistemdeki sayıyı onluk sisteme çeviren python programı
import sys

binary = int(input("İkilik sistemdeki sayıyı giriniz :"))
cBinary = binary
sayac = 0
decimal = 0
while cBinary > 0:
    temp = cBinary % 10
    if temp > 1 :
        print("Lütfen binary sayı giriniz ! ")
        sys.exit()
    cBinary = int(cBinary / 10)
    decimal += temp * pow(2,sayac)
    sayac += 1

print("Decimal : ",decimal)
