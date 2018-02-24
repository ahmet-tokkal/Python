#E sayısının  istenilen adım sayısı kadar kuvvetini hesaplayan c programı

def faktoriyelAl(n):
    if n <= 0:
        return 1
    else :
        return (n * faktoriyelAl(n-1))

kuvvet = int(input("Kuvveti giriniz :"))
adim = int(input("Adım sayısını giriniz :"))

toplam = 1.0
kismiToplam = 0.0

for i in range(1,adim+1):
    kismiToplam = pow(kuvvet,i)/faktoriyelAl(i)
    toplam += kismiToplam
print("e ^",kuvvet," = ",toplam,)
