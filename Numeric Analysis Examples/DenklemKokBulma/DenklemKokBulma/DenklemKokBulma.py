import sys
import math
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Tasarim import *

class Pencere(QMainWindow,Ui_Form):
    def __init__(self):
        super(Pencere, self).__init__()
        self.setupUi(self)
        self.Arayuz()

    def Arayuz(self):
        self.AktiflikDurumu(False,False,False,False)
     
        self.btnSec.clicked.connect(lambda: self.Sec(self.cmbBxFonksiyon.currentIndex(),
                                                     self.cmbBoxYontem.currentText()))

    def Sec(self, fonksiyon, yontem):
        if yontem == "Fixed Point":
                self.AktiflikDurumu(True,False,True,False)
        elif yontem== "Bisection":
                self.AktiflikDurumu(True,False,True,False)
        elif yontem == "Newton Repson":
                self.AktiflikDurumu(False,True,True,False)
        elif yontem == "Secant":
                self.AktiflikDurumu(False,True,True,False)
               
        self.btnHesapla.clicked.connect(lambda: self.Hesapla(fonksiyon, self.lnEdtA.text(),self.lnEdtB.text(),self.lnEdtAdimSayisi.text()))
        self.btnTemizle.clicked.connect(lambda: self.Temizle())    

    def Hesapla(self,fnksyn,a,b,adimSayisi):
        # Kullanıcı kutuları boş bırakırsa
        if a == ""  or b == "" or adimSayisi == "":
            hataMesaji = QMessageBox.warning(self,"Hata","Lütfen değerleri giriniz !",QMessageBox.Ok,QMessageBox.Ok)
        
        # Kullanıcı karakter girerse
        elif a.isalpha() or b.isalpha() or adimSayisi.isalpha():
            hataMesaji = QMessageBox.warning(self,"Hata","Lütfen sayı giriniz !",QMessageBox.Ok,QMessageBox.Ok) 
 
        else:
            # Swap işlemi
            if a > b:
                a,b = b,a
            if self.cmbBoxYontem.currentText() == "Fixed Point":
                self.lnEdtSonuc.setText(self.FixedPointHesapla(fnksyn,a,b,adimSayisi))
                self.AktiflikDurumu(True,False,True,True)     
            elif self.cmbBoxYontem.currentText() == "Bisection":
                self.lnEdtSonuc.setText(self.BisectionHesapla(fnksyn,a,b,adimSayisi))
                self.AktiflikDurumu(True,False,True,True)     
            elif self.cmbBoxYontem.currentText() == "Newton Repson":
                self.lnEdtSonuc.setText(self.NewtonRepsonHesapla(fnksyn,a,b,adimSayisi))
                self.AktiflikDurumu(False,True,True,True)
            elif self.cmbBoxYontem.currentText() == "Secant":
                self.lnEdtSonuc.setText(self.SecantHesapla(fnksyn,a,b,adimSayisi)) 
                self.AktiflikDurumu(False,True,True,True)     
                
    def Temizle(self):
        # Kutuları Temizleme
        self.lnEdtA.clear()
        self.lnEdtB.clear()
        self.lnEdtAdimSayisi.clear()
        self.lnEdtSonuc.clear()

    def FixedPointHesapla(self,fnksyn,a,b,adim):
        i = 0
        x = a
        try :
            while i < int(adim):
                fx = float(self.Fonksiyonlar(fnksyn,x))
                gx = float(self.GFonksiyonlar(fnksyn,a,b,x))
                print("gx : "+str(gx))
                x = gx
                i+=1
            return str(fx) 
        except Exception:
            print("hata var")

    def BisectionHesapla(self,fnksyn,a,b,adim):
        fa = self.Fonksiyonlar(fnksyn,a);
        fb = self.Fonksiyonlar(fnksyn,b);
        i=0
        x = a
        y = b
        z = 0
        if(fa*fb < 0):
            while i < int(adim):
                z = (float(x)+ float(y))/2
                fx = self.Fonksiyonlar(fnksyn,z)
                if(fx*fa > 0):
                    fa = fx
                    x = z
                else:
                    fb = fx
                    y = z
                i+=1
                print(fx)
            return str(fx)
        else:
            hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta kök yok.",QMessageBox.Ok,QMessageBox.Ok)   

    def NewtonRepsonHesapla(self,fnksyn,a,b,adim):
        x = int(a)
        hataPayi = float(adim)
        sonuc = 0
        if(float(adim)<0):
            while hataPayi <= float(adim):
                fx = self.Fonksiyonlar(fnksyn,x)
                print("fx :" + str(fx))
                fxt = self.FonksiyonTurev(fnksyn,x)
                print("fxt :" + str(fxt))
                hataPayi = float(fx)/float(fxt)
                print("HtP :" + str(hataPayi))
                sonuc = x - hataPayi
                print(sonuc)
                x = sonuc
        else:
            while hataPayi >= float(adim):
                fx = self.Fonksiyonlar(fnksyn,x)
                print("fx :" + str(fx))
                fxt = self.FonksiyonTurev(fnksyn,x)
                print("fxt :" + str(fxt))
                hataPayi = float(fx)/float(fxt)
                print("HtP :" + str(hataPayi))
                sonuc = x - hataPayi
                print(sonuc)
                x = sonuc
        return str(sonuc)

    def SecantHesapla(self,fnksyn,a,b,adim):
        return(1)

    def Fonksiyonlar(self,fnk, x):
        if fnk == 0:
            return pow(float(x),3) + (3 *  float(x)) - 20 
        elif fnk == 1:
            return  pow(float(x),3) - (2 *  float(x))+ 1 
        elif fnk == 2:
            return   float(x) - math.sqrt(float(x) +  6) 
        elif fnk == 3:
            return   (pow(float(x),2)-float(x)) / 3
        elif fnk == 4:
            return   pow(float(x),3) - 20*float(x)
    def GFonksiyonlar(self,fnk,a,b,x):
        if fnk == 0:
            gx = (pow(float(x),3) - 20) / 3 
            if(not (gx >= float(a) and gx <= float(b))):
                gx = math.pow((20-3*float(x)),1/3)
                if(not (gx >= float(a) and gx <= float(b))):
                     hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta bu fonsiyonu hesaplayamadım!!!",QMessageBox.Ok,QMessageBox.Ok)
            elif((gx >= float(a) and gx <= float(b))):
                return gx
            else :
                hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta bu fonsiyonu hesaplayamadım!!!",QMessageBox.Ok,QMessageBox.Ok)
        elif fnk == 1:
            gx = (pow(float(x),3) + 1) / 2 
            if(not (gx >= float(a) and gx <= float(b))):
                gx = math.pow((2*float(x)-1),1/3)
                if(not (gx >= float(a) and gx <= float(b))):
                     hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta bu fonsiyonu hesaplayamadım!!!",QMessageBox.Ok,QMessageBox.Ok)
            elif((gx >= float(a) and gx <= float(b))):
                return gx
            else :
                hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta bu fonsiyonu hesaplayamadım!!!",QMessageBox.Ok,QMessageBox.Ok)
        elif fnk == 2:
            gx = math.sqrt(float(x)+6) 
            if(not (gx >= float(a) and gx <= float(b))):
                gx = pow(float(x),2)+-6
                if(not (gx >= float(a) and gx <= float(b))):
                     hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta bu fonsiyonu hesaplayamadım!!!",QMessageBox.Ok,QMessageBox.Ok)
            elif((gx >= float(a) and gx <= float(b))):
                return gx
            else :
                hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta bu fonsiyonu hesaplayamadım!!!",QMessageBox.Ok,QMessageBox.Ok)
        elif fnk == 3:
            gx = pow(float(x),2) 
            if(not (gx >= float(a) and gx <= float(b))):
                gx = math.sqrt(float(x))
                if(not (gx >= float(a) and gx <= float(b))):
                     hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta bu fonsiyonu hesaplayamadım!!!",QMessageBox.Ok,QMessageBox.Ok)
            elif((gx >= float(a) and gx <= float(b))):
                return gx
            else :
                hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta bu fonsiyonu hesaplayamadım!!!",QMessageBox.Ok,QMessageBox.Ok)
        elif fnk == 4:
            gx = pow(float(x),3)/20 
            if(not (gx >= float(a) and gx <= float(b))):
                gx = pow(20*float(x),1/3)
                if(not (gx >= float(a) and gx <= float(b))):
                     hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta bu fonsiyonu hesaplayamadım!!!",QMessageBox.Ok,QMessageBox.Ok)
            elif((gx >= float(a) and gx <= float(b))):
                return gx 
            else :
                hataMesaji = QMessageBox.warning(self,"Hata","Bu aralıkta bu fonsiyonu hesaplayamadım!!!",QMessageBox.Ok,QMessageBox.Ok)  
    def FonksiyonTurev(self,fnk,x):
        if fnk == 0:
            return 3 * pow(float(x),2) + 3
        elif fnk == 1:
            return 3 * pow(float(x),2) - 2
        elif fnk == 2:
            return  1 - 1 / (2* math.sqrt(x+6))
        elif fnk == 3:
            return   (2*x-1) /3
        elif fnk == 4:
            return  3 * pow(float(x),2) - 20
    def AktiflikDurumu(self, drm1, drm2,drm3,drm4):
        self.lblA.setVisible(drm1)
        self.lblB.setVisible(drm1)
        self.lblx0.setVisible(drm2)
        self.lblx1.setVisible(drm2)
        self.lnEdtA.setVisible(drm3)
        self.lnEdtB.setVisible(drm3)
        self.lblAdimSayisi.setVisible(drm1)
        self.lblHataPayi.setVisible(drm2)
        self.lnEdtAdimSayisi.setVisible(drm3)
        self.btnHesapla.setVisible(drm3)
        self.btnTemizle.setVisible(drm3)
        self.lblSonuc.setVisible(drm4)
        self.lnEdtSonuc.setVisible(drm4)

def Main():
    app = QApplication(sys.argv)
    GUI = Pencere()
    GUI.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    Main()