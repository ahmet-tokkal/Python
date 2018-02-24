import os
from Matris import Matris 
print("""
-----------------------------------------------
---       Matriste İşlemler                 ---
-----------------------------------------------       
--- Toplama işlemi için --> 1               ---
--- Çıkarma işlemi için --> 2               ---
--- Çarpma işlemi için --> 3                ---
--- Tersini alma işlemi için --> 4          ---
--- Ortogonal sorgulama için --> 5          ---
--- Transpoze işlemi için --> 6             ---
--- Determinant hesaplamak için --> 7       ---
--- Çıkmak için --> 8                       ---
-----------------------------------------------
""")
soru ="Yapmak istediginiz islem : "
islem = input(soru)
if(islem =="1"):
    os.system("cls")
    print("Toplama işlemini seçtin")
    satir1 = input("1.Matrisin satir sayisini gir :")
    sutun1 = input("1.Matrisin sutun sayisi gir :")

    satir2 = input("2.Matrisin satir sayisini gir :")
    sutun2 = input("2.Matrisin sutun sayisi gir :")
    
    if satir1 == satir2 and sutun1 == sutun2 :
        os.system("cls")
        matris1= Matris(satir1,sutun1)
        matris1.MatrisiAl()
        print("{:^30}".format("Matris 1"))
        matris1.MatrisiYaz()
        matris2=Matris(satir2,sutun2)
        matris2.MatrisiAl()
        print("{:^30}".format("Matris 2"))
        matris2.MatrisiYaz()
        matris3 = matris1.MatrisTopla(matris2)
        print("{:^30}".format("Sonuç Matrisi"))
        matris3.MatrisiYaz()
    else:
        print("Matrislerde toplama işlemi yapabilmek için matrislerin satır ve sütun sayıları eşit olmalı !")
elif(islem=="2"):
    os.system("cls")
    print("Çıkarma işlemini seçtin")
    satir1 = input("1.Matrisin satir sayisini gir :")
    sutun1 = input("1.Matrisin sutun sayisi gir :")

    satir2 = input("2.Matrisin satir sayisini gir :")
    sutun2 = input("2.Matrisin sutun sayisi gir :")
    
    if satir1 == satir2 and sutun1 == sutun2 :
        os.system("cls")
        matris1= Matris(satir1,sutun1)
        matris1.MatrisiAl()
        print("{:^30}".format("Matris 1"))
        matris1.MatrisiYaz()
        matris2=Matris(satir2,sutun2)
        matris2.MatrisiAl()
        print("{:^30}".format("Matris 2"))
        matris2.MatrisiYaz()
        matris3 = matris1.MatrisCikar(matris2)
        print("{:^30}".format("Sonuç Matrisi"))
        matris3.MatrisiYaz()
    else:
        print("Matrislerde çıkarma işlemi yapabilmek için matrislerin satır ve sütun sayıları eşit olmalı !")
elif(islem=="3"):
    os.system("cls")
    print("Çarpma işlemini seçtin")
    satir1 = input("1.Matrisin satir sayisini gir :")
    sutun1 = input("1.Matrisin sutun sayisi gir :")

    satir2 = input("2.Matrisin satir sayisini gir :")
    sutun2 = input("2.Matrisin sutun sayisi gir :")
    os.system("cls")
    if sutun1 == satir2:
        matris1= Matris(satir1,sutun1)
        matris1.MatrisiAl()
        print("{:^30}".format("Matris 1"))
        matris1.MatrisiYaz()
        matris2=Matris(satir2,sutun2)
        matris2.MatrisiAl()
        print("{:^30}".format("Matris 2"))
        matris2.MatrisiYaz()
        matris3 = matris1.MatrisCarp(matris2)
        print("{:^30}".format("Sonuç Matrisi"))
        matris3.MatrisiYaz()
    else:
        print("Matriste çarpma işlemi yapabilmek için 1.matrisin sutun sayısı 2.matrisin satır sayısına eşit olmalıdır !")
elif(islem=="4"):
    os.system("cls")
    print("Tersini alma işlemini seçtin")
    satir1 = input("1.Matrisin satir sayisini gir :")
    sutun1 = input("1.Matrisin sutun sayisi gir :")
    if int(satir1) > 1 and int(sutun1) > 1  and satir1 == sutun1:
        os.system("cls")
        matris1= Matris(satir1,sutun1)
        matris1.MatrisiAl()
        print("{:^30}".format("Matrisin Normal Hali"))
        matris1.MatrisiYaz()
        print("{:^30}".format("Matrisin Tersi"))
        Matris.MatrisinTersiniAl(matris1)
    else:
        print("Bir matrisin tersinin alınabilmesi için kare matris olması gerekmektedir.")    
elif(islem=="5"):
    os.system("cls")
    print("Ortogonal sorgulama işlemini seçtin")
    satir1 = input("Matrisin satir sayisini gir :")
    sutun1 = input("Matrisin sutun sayisi gir :")
    if satir1==sutun1:
        os.system("cls")
        matris1= Matris(satir1,sutun1)
        matris1.MatrisiAl()
        print("{:^30}".format("Matrisin Normal Hali"))
        matris1.MatrisiYaz()
        print("*"*30)
        matris1.OrtogonalMatris()
    else:
        print("Bir matris ortogonal olabilmesi için kare matris olması lazım!")
elif(islem=="6"):
    os.system("cls")
    print("Transpoze işlemini seçtin")
    satir1 = input("Matrisin satir sayisini gir :")
    sutun1 = input("Matrisin sutun sayisi gir :")
    os.system("cls")
    matris1= Matris(satir1,sutun1)
    matris1.MatrisiAl()
    print("{:^30}".format("Matrisin Normal Hali"))
    matris1.MatrisiYaz()
    matrisT=matris1.MatrisinTranspozesi()
    print("{:^30}".format("Matrisin Transpoze Hali"))
    matrisT.MatrisiYaz()
elif(islem=="7"):
    os.system("cls")
    print("Determinant hesaplama işlemini seçtin")
    satir1 = input("Matrisin satir sayisini gir :")
    sutun1 = input("Matrisin sutun sayisi gir :")
    if satir1==sutun1:
        os.system("cls")
        matris1= Matris(satir1,sutun1)
        matris1.MatrisiAl()
        print("{:^30}".format("Matrisin Normal Hali"))
        matris1.MatrisiYaz()
        print("Matrisin determinantı :",Matris.DeterminantAl(matris1))
    else:
        print("Matrisin determinantının alınabilmesi için kare matris olması gerekli.")
elif(islem=="8"):
    exit()
else :
    print("Yanlış bir değer girdin")



