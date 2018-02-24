import sys,os,copy
from Matris import Matris
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Tasarim import Ui_Form

class Pencere(QMainWindow,Ui_Form):
    def __init__(self):
        super(Pencere, self).__init__()
        self.setupUi(self)
        self.Arayuz()

    def Arayuz(self):
        self.SonucDurum(False)
        self.btnHesapla.clicked.connect(lambda: self.Hesapla(self.lnEdtDenklem1.text(),
                                               self.lnEdtDenklem2.text(),
                                               self.lnEdtDenklem3.text(),
                                               self.lnEdtDenklem4.text(),
                                               self.cmbBxYontem.currentIndex()))
        self.btnTemizle.clicked.connect(lambda:self.Temizle())
       
    def SonucDurum(self,durum):
        self.lblx.setVisible(durum)
        self.lbly.setVisible(durum)
        self.lblz.setVisible(durum)
        self.lblt.setVisible(durum)
        self.lnEdtX.setVisible(durum)
        self.lnEdtY.setVisible(durum)
        self.lnEdtZ.setVisible(durum)
        self.lnEdtT.setVisible(durum)

    def SonucYaz(self,sonuc):
        self.lnEdtX.setText(str(sonuc[0]))
        self.lnEdtY.setText(str(sonuc[1]))
        self.lnEdtZ.setText(str(sonuc[2]))
        self.lnEdtT.setText(str(sonuc[3]))

    def Hesapla(self,denklem1,denklem2,denklem3,denklem4,yontem):
        if(denklem1=="" or denklem2=="" or denklem3=="" or denklem4==""):
                hataMesaji = QMessageBox.warning(self,"Hata","Lütfen denklemleri giriniz !",QMessageBox.Ok,QMessageBox.Ok)
        else:    
            x1 = self.DenklemParcala(denklem1)
            x2 = self.DenklemParcala(denklem2)
            x3 = self.DenklemParcala(denklem3)
            x4 = self.DenklemParcala(denklem4)
            print(x1+x2+x3+x4)
            y1=x1[4]
            y2=x2[4]
            y3=x3[4]
            y4=x4[4]
            x1.pop(4)
            x2.pop(4)
            x3.pop(4)
            x4.pop(4)
            matris = x1+x2+x3+x4
            smatris =[y1,y2,y3,y4]   
            print(matris)
            print(smatris)

            mtrs = Matris(4,4)
            a=0
            for k in range(4):
                for l in range(4):
                   mtrs.matris[k][l]=int(matris[a])
                   a+=1
            smtrs = Matris(4,1)
            for i in range(4):
                    smtrs.matris[i][0]=int(smatris[i])    
          
            if(yontem == 0):
                self.CramerYontemi(mtrs,smtrs)
            elif(yontem == 1):
                self.GaussYontemi(mtrs,smtrs)
            else:
                self.CholeskyYontemi(mtrs,smtrs)

    def DenklemParcala(self,denklem):
        rakamlar = ""
        for i in denklem:
            if(i.isdigit() or i == "+" or i=="-" or i=="="):
                rakamlar += i
            elif(i.isspace()):
                continue
            else:
                rakamlar += " "
        print(rakamlar)
        degiskenler=["","","","",""]
        sayac =0
        for i in range(len(rakamlar)):
            if(sayac<=4):
                if(rakamlar[i].isspace()):
                    sayac+=1
                    continue
                elif (rakamlar[i]=="+" or rakamlar[i]=="="):
                    continue
                else:
                    degiskenler[sayac]+= rakamlar[i]
            else:
                hataMesaji = QMessageBox.warning(self,"Hata","Lütfen maximum dört bilinmeyenli bir denklem giriniz !",QMessageBox.Ok,QMessageBox.Ok)
                self.Temizle()
                break 
        return degiskenler

    def Temizle(self):
            self.lnEdtDenklem1.clear()
            self.lnEdtDenklem2.clear()        
            self.lnEdtDenklem3.clear()  
            self.lnEdtDenklem4.clear()      
            self.cmbBxYontem.setCurrentIndex(0)
            self.SonucDurum(False)
            os.system("cls")

    def CramerYontemi(self,degerMtrs,sonucMtrs):
        print("CramerYontemi") 
        det = Matris.DeterminantAl(degerMtrs)
        print(det)
        sonuc = []
        geciciMtrs = Matris(4,4)
        geciciMtrs.matris =copy.deepcopy(degerMtrs.matris)
        geciciMtrs.MatrisiYaz()
        for k in range(4):
               geciciMtrs.matris =copy.deepcopy(degerMtrs.matris)
               for l in range(4):
                  geciciMtrs.matris[l][k]=sonucMtrs.matris[l][0]
               sonuc.append(Matris.DeterminantAl(geciciMtrs)/det)
               geciciMtrs.MatrisiYaz()
        self.SonucYaz(sonuc)
        self.SonucDurum(True)

    def GaussYontemi(self,degerMtrs,sonucMtrs):
        print("GaussJordanYontemi") 
        degerMtrs.MatrisiYaz()
        sonucMtrs.MatrisiYaz()
    def CholeskyYontemi(self,degerMtrs,sonucMtrs):
        print("Cholesky Yöntemi")     
        degerMtrs.MatrisiYaz()
        sonucMtrs.MatrisiYaz()
def Main():
    app = QApplication(sys.argv)
    GUI = Pencere()
    GUI.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    Main()