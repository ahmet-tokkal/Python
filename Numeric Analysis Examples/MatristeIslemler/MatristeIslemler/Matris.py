class Matris(object):
    def __init__(self,satir,sutun):
        # Matrisin yapıcısı alınan parametreye göre boş matris oluşturur.
        self.satir = satir
        self.sutun = sutun
        self.matris = []
        for i in range(int(satir)):
            self.matris += [ [0] * int(sutun)]

    def MatrisiYaz(self):
        # Matrisi ekrana yazar
        print("*"*30)
        for i in range(int(self.satir)):
            for j in range(int(self.sutun)):
                print(self.matris[i][j],end=" ")
            print()
        print("*"*30)

    def MatrisiAl(self):
        # Kullanıcıdan matrisi alır
        print("*"*30)
        for k in range(int(self.satir)):
            for l in range(int(self.sutun)):
                metin = "Matris["+str(k)+"]["+str(l)+"] degerini gir :"
                self.matris[k][l] = input(metin)
        print("*"*30)

    def MatrisTopla(self,matris2):
        # Matris toplama işlemi 
        sonuc = Matris(self.satir,self.sutun)
        for i in range(int(sonuc.satir)):
            for j in range(int(sonuc.sutun)):
                sonuc.matris[i][j]= int(self.matris[i][j])+int(matris2.matris[i][j])
        return sonuc

    def MatrisCikar(self,matris2):
        # Matris çıkarma işlemi 
        sonuc = Matris(self.satir,self.sutun)
        for i in range(int(sonuc.satir)):
            for j in range(int(sonuc.sutun)):
                sonuc.matris[i][j]= int(self.matris[i][j])-int(matris2.matris[i][j])
        return sonuc

    def MatrisCarp(self,matris2):
        # Matris çarpma işlemi
        sonuc = Matris(self.satir,matris2.sutun)
        carpim = 0
        for i in range(int(sonuc.satir)):
            for j in range(int(sonuc.sutun)):
                for k in range(int(self.sutun)):
                    carpim += int(self.matris[i][k])*int(matris2.matris[k][j])
                sonuc.matris[i][j] = carpim
                carpim = 0
        return sonuc   

    def MatrisinTranspozesi(self):
        # Matrisin transpozini alma yani devirme 
        sonuc = Matris(self.sutun, self.satir)
        for i in range(int(sonuc.satir)):
            for j in range(int(sonuc.sutun)):
                sonuc.matris[i][j]=self.matris[j][i]
        return sonuc
   
    def BirimMatrisOlustur(self):
        # diğer metotlarda kullanılmak üzere birim matris oluşturma
        # Varsayılan olarak oluşan 0 matrisini birim matrise çevirir
        for i in range(int(self.satir)):
            self.matris[i][i] = 1

    def OrtogonalMatris(self):
        # Girilen matrisin birim matris olup olmadığını sorgular
        # Matrisi transpozesiyle çarpıp birim matrise eşit olup olmadığını kontrol eder
        birimMatris = Matris(self.satir,self.sutun)
        birimMatris.BirimMatrisOlustur()
        
        self.matris = self.MatrisCarp(self.MatrisinTranspozesi())
        if self.matris.MatrisKarsilastir(birimMatris):
            print("Bu matris Ortagonal bir matristir.")
        else:
            print("Bu matris Ortagonal bir matris değildir.")

    def MatrisKarsilastir(self,mtrs2):
        # İki matrisin eşit olup olmadığını kontrol eder
        for i in range(int(self.satir)):
            for j in range(int(self.sutun)):
                if self.matris != mtrs2.matris :
                    return False
                else:
                    continue 
        return True

    def MatrisKucult(self,indis):
        # determinatta kullanılmak üzere matrisi küçültür.
        x = -1
        y = 0
        yeniMtrs = Matris(int(self.satir)-1,int(self.sutun)-1)
        for i in range(int(self.satir)):
            if i == 0:
                continue
            y = 0
            x = x + 1              
            for j in range(int(self.sutun)):
                if j== indis:
                    continue
                yeniMtrs.matris[x][y]=self.matris[i][j]
                y = y + 1
        return yeniMtrs 
    
    @classmethod
    def DeterminantAl(cls,mtrs):
        det = 0
        if len(mtrs.matris) == 1:
                return mtrs.matris[0][0]
        else :
            for i in range(int(mtrs.sutun)):
                   det += int(mtrs.matris[0][i]) * int(pow((-1),(2+i))) * int(Matris.DeterminantAl(mtrs.MatrisKucult(i)))
            return det

    @classmethod
    def MatrisinTersiniAl(cls,mtrs):
        brmMtrs = Matris(mtrs.satir,mtrs.sutun)
        brmMtrs.BirimMatrisOlustur()
        for i in range(int(mtrs.satir)):
            a = mtrs.matris[i][i]
            for j in range(int(mtrs.sutun)):
                mtrs.matris[i][j] = float(mtrs.matris[i][j])/float(a)
                brmMtrs.matris[i][j]=float(brmMtrs.matris[i][j])/float(a)
            for j in range(int(mtrs.sutun)):
                if j != i:
                    b = mtrs.matris[j][i]
                    for k in range(int(mtrs.sutun)):
                        mtrs.matris[j][k] = float(mtrs.matris[j][k])-(float(mtrs.matris[i][k])*float(b))
                        brmMtrs.matris[j][k] = float(brmMtrs.matris[j][k])-(float(brmMtrs.matris[i][k])*float(b))
        brmMtrs.MatrisiYaz()
                    
            
                
                
            
                        
                    