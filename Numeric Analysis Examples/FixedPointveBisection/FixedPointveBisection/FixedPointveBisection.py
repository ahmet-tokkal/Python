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
        self.btnTemizle.clicked.connect(self.Temizle)
        self.btnHesapla.clicked.connect(lambda: self.Hesapla(self.lnEdtA.text(),
                                                        self.lnEdtB.text(),
                                                        self.lnEdtAdimSayisi.text(),
                                                        self.btnTemizle))

    
    def Hesapla(self,a,b,adimSayisi,btnTemizle):
        btnTemizle.setEnabled(True)
        # Swap işlemi
        if a > b:
            a,b = b,a
        
        # Kullanıcı kutuları boş bırakırsa
        if a == ""  or b == "" or adimSayisi == "":
            hataMesaji = QMessageBox.warning(self,"Hata","Lütfen değerleri giriniz !",QMessageBox.Ok,QMessageBox.Ok)
        
        # Kullanıcı karakter girerse
        elif a.isalpha() or b.isalpha() or adimSayisi.isalpha():
            hataMesaji = QMessageBox.warning(self,"Hata","Lütfen sayı giriniz !",QMessageBox.Ok,QMessageBox.Ok) 
        
        else:
            if self.cmbBoxYontem.currentText() == "Fixed Point":
                self.lcdSonuc.display(self.FixedPointHesapla(a,b,adimSayisi))
            else:
                self.lcdSonuc.display(self.BisectionHesapla(a,b,adimSayisi))
                
    def Temizle(self,):
        # Kutuları Temizleme
        self.lnEdtA.clear()
        self.lnEdtB.clear()
        self.lnEdtAdimSayisi.clear()
        self.lcdSonuc.display(0)

    def FixedPointHesapla(self,a,b,adim):
        i = 0
        x = 1.5
        fx=gx=0
        while i < int(adim) :
            gx = pow((3*x+20),1/3)
            fx = pow(gx,3)-3*gx-20
            x = gx
            i +=1  
        print(fx)
        return fx
        

    def BisectionHesapla(self,a,b,adim):
        return(1)
        
def Main():
    app = QApplication(sys.argv)
    GUI = Pencere()
    GUI.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    Main()