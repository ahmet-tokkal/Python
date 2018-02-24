#Yarıçapı verilen çemberin çapı, çevresi ve alanını hesaplayan python programı

yaricap = int(input("Yarıçapı giriniz : "))

piSayisi = 3.14159
cap = yaricap * 2
cevre = 2 * piSayisi * yaricap
alan = 2 * pow(yaricap,2)

print("Çemberin Çapı : ",cap)
print("Çemberin Çevresi : ",cevre)
print("Çemberin Alanı : ",alan)
