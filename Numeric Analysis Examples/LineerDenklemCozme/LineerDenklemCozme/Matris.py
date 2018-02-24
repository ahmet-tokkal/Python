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

    def BirimMatrisOlustur(self):
        # diğer metotlarda kullanılmak üzere birim matris oluşturma
        # Varsayılan olarak oluşan 0 matrisini birim matrise çevirir
        for i in range(int(self.satir)):
            self.matris[i][i] = 1

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
                    
            
                
                
            
                        
                    