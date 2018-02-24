#Kullanıcıdan alınan pozitif sayının faktoriyelini recursive şekilde bulan python programı

def faktoriyelAl(n):
    if n <= 0:
        return 1
    else :
        return (n * faktoriyelAl(n-1))

sayi  = int(input("Pozitif bir sayi giriniz :"))
if sayi < 0:
    print("Lütfen pozitif bir sayi giriniz!")
else :
    print(sayi,"! = ",faktoriyelAl(sayi))
