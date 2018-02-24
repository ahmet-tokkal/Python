#Girilen 10 sayıdan dizisiz en büyüğünü bulan C programı

enBuyukSayi =0
for i in range(1,11):
    sayi = int(input("%d.Sayıyı giriniz :" %(i)))
    if sayi > enBuyukSayi:
        enBuyukSayi=sayi
print("En büyük sayi : ",enBuyukSayi)
