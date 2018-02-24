#Kullanıcının girdiği sayının polindrome(tersi aynı) olup olmadığını bulan python programı

sayi = int(input("Sayıyı giriniz :"))
cSayi = sayi
polindrome=0

while cSayi > 10:
    temp = int(cSayi % 10)
    cSayi /= 10
    polindrome += temp
    polindrome *= 10
polindrome +=int(cSayi)
print(polindrome)
if polindrome == sayi:
    print("Girilen sayı polindrome bir sayıdır.")
else:
    print("Girilen sayı polindrome bir sayı değildir.")
