#Kullanıcıdan kaç litre benzin ve kaç km yol aldığını alıp her litre için kaç km yol aldığını hesaplayan ve girilen
#tüm bilgilerden sonra toplam gidilen km için harcanan benzin miktarını bulan python programı

i = 0
toplamOran=0
harcananBenzin = 0
while harcananBenzin >= 0:
    harcananBenzin = float(input("Kaç litre benzin harcandı(Çıkış için -1):"))
    if harcananBenzin == -1:
        break
    else:
        alinanYol = float(input("Kaç km yol alındı :"))
        oran = alinanYol/harcananBenzin
        print("1 litre benzi ile alınan yol : ",oran)
        toplamOran += oran
        i += 1

print("Toplam ortalama km/litre :",(toplamOran/i))


