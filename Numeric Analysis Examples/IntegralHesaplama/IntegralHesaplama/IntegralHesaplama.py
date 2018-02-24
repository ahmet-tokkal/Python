import sys
import math
# GUI için gerekli kütüphaneler 
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Pencere(QMainWindow):
    def __init__(self):
        super(Pencere,self).__init__()
        self.setGeometry(300,300,1000,500) # Pencerenin konumunu ve boyutunu 
        self.setStyleSheet("Background-color : #2EFE9A") # Pencere arkaplanı
        self.setWindowTitle("Integral Hesaplama") # Pencere başlığını ayarlama
        self.setWindowIcon(QIcon("integral.png")) # Pencere ikonu ayarlama
        
        self.statusBar() # Durum Çubuğu oluşturma
        
        self.Arayuz()

    def Arayuz(self):
        # Program başlığı labelı oluşturma ayarlama
        lblBaslik = QLabel("İntegral Hesaplama Programı ",self)
        lblBaslik.setFont(QFont("Comic Sans MS",18))
        lblBaslik.setStyleSheet("color :red")
        lblBaslik.setGeometry(300,0,400,50)

        # Fonsiyon labelı oluşturma ayarlama
        lblFonksiyon = QLabel("Fonksiyon Seç :",self)
        lblFonksiyon.setFont(QFont("Comic Sans MS",12))
        lblFonksiyon.setStyleSheet("color : yellow ; font-weight: bold")
        lblFonksiyon.setGeometry(10,70,500,50)
        
        # Fonksiyonların bulunduğu comboboxı oluşturma ayarlama
        CmbBxFonksiyon = QComboBox(self)
        CmbBxFonksiyon.addItem("(13(x-x^(2)))/√(e^3x )") # öge ekleme
        CmbBxFonksiyon.addItem("e^x")
        CmbBxFonksiyon.addItem("x*sinx")
        CmbBxFonksiyon.addItem("(x^2)+4")
        CmbBxFonksiyon.addItem("4/(1+x^2)")
        CmbBxFonksiyon.setFont(QFont("Comic Sans MS",12))
        CmbBxFonksiyon.setStyleSheet("background-color: white; color : black")   
        CmbBxFonksiyon.setGeometry(180,70,250,50)
        
        # Yöntem labelı oluşturma ayarlama
        lblYontem = QLabel("Yöntem Seç   :",self)
        lblYontem.setFont(QFont("Comic Sans MS",12))
        lblYontem.setStyleSheet("color : yellow ; font-weight: bold")
        lblYontem.setGeometry(10,145,500,50)
    
        # yöntemlerin bulunduğu comboboxı oluşturma ayarlama
        CmbBxYontem = QComboBox(self)
        CmbBxYontem.addItem("Dikdörtgen Kuralı")
        CmbBxYontem.addItem("Orta Dikdörtgen Kuralı")
        CmbBxYontem.addItem("Yamuk Kuralı")
        CmbBxYontem.addItem("Simpson Kuralı")  
        CmbBxYontem.setFont(QFont("Comic Sans MS",12))
        CmbBxYontem.setStyleSheet("background-color: white; color : black")   
        CmbBxYontem.setGeometry(180,145,250,50)      
        
        # A labelı oluşturma ayarlama
        lblA = QLabel("A :",self)
        lblA.setFont(QFont("Comic Sans MS",12))
        lblA.setStyleSheet("color : yellow ; font-weight: bold")
        lblA.setGeometry(180,210,50,50)  
        
        # A LineEdit oluşturma ayarlama
        lnEdtA=QLineEdit(self)
        lnEdtA.setFont(QFont("Comic Sans MS",12))
        lnEdtA.setStyleSheet("background-color: white; color : black")
        lnEdtA.setGeometry(220,220,80,30)    
        
        # B labelı oluşturma ayarlama    
        lblB = QLabel("B :",self)
        lblB.setFont(QFont("Comic Sans MS",12))
        lblB.setStyleSheet("color : yellow ; font-weight: bold")
        lblB.setGeometry(310,210,50,50)  
      
        # B LineEdit oluşturma ayarlama
        lnEdtB=QLineEdit(self)
        lnEdtB.setFont(QFont("Comic Sans MS",12))
        lnEdtB.setStyleSheet("background-color: white; color : black")   
        lnEdtB.setGeometry(350,220,80,30)
        
        # Adim Sayısı labelı oluşturma ayarlama
        lblAdim = QLabel("Adım Sayısı   :",self)
        lblAdim.setFont(QFont("Comic Sans MS",12))
        lblAdim.setStyleSheet("color : yellow ; font-weight: bold")
        lblAdim.setGeometry(10,270,150,50)    

        # Adim Sayısı LineEdit oluşturma ayarlama
        lnEdtAdim=QLineEdit(self)
        lnEdtAdim.setFont(QFont("Comic Sans MS",12))
        lnEdtAdim.setStyleSheet("background-color: white; color : black")   
        lnEdtAdim.setGeometry(180,280,80,30)
        
        #Progress Bar oluşturma ve ayarlama    
        self.prgBrIslem = QProgressBar(self)
        self.prgBrIslem.setGeometry(700,470,300,20)
        
         # Temizle butonu oluşturma ayarlama
        btnTemizle = QPushButton("Temizle",self)
        btnTemizle.setEnabled(False)
        btnTemizle.setFont(QFont("Comic Sans MS",12))
        btnTemizle.setGeometry(330,345,100,50)
        btnTemizle.setStyleSheet("background-color: red; color : white")  
        btnTemizle.setStatusTip("Ekranı temizle") # durum çubuğuna yazı yazma
        btnTemizle.clicked.connect(lambda: self.Temizle(lnEdtA,lnEdtB,lnEdtAdim,self.prgBrIslem))  # tıklandığında çalışacak fonksiyon

        # Hesapla butonu oluşturma ayarlama
        btnHesapla = QPushButton("Hesapla",self)
        btnHesapla.setFont(QFont("Comic Sans MS",12))
        btnHesapla.setGeometry(180,345,100,50)
        btnHesapla.setStyleSheet("background-color: blue; color : white")
        btnHesapla.setStatusTip("Fonksiyonun integralini hesapla") # durum çubuğuna yazı yazma
        btnHesapla.clicked.connect(lambda: self.Hesapla(CmbBxFonksiyon.currentText(), # tıklandığında çalışacak fonksiyon
                                                        CmbBxYontem.currentText(),
                                                        lnEdtA.text(),
                                                        lnEdtB.text(),
                                                        lnEdtAdim.text(),
                                                        btnTemizle))
       
        

               
        self.show()

    def Hesapla(self, seciliFonksiyon,seciliYontem,a,b,adimSayisi,btnTemizle):
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
            global lblSonucTanim
            lblSonucTanim = QLabel("F(x) = "+seciliFonksiyon+" ifadesininin " +a+" - "+b+" aralığında \n"+
                               seciliYontem+" yöntemine göre "+adimSayisi+" adımdaki : "  ,self)
            lblSonucTanim.setFont(QFont("Comic Sans MS",12))
            lblSonucTanim.setStyleSheet("color :blue")
            lblSonucTanim.setGeometry(450,50,20000,100)
            lblSonucTanim.show()
            
            # Secilen yönteme göre fonksiyonun hesaplanması ve ekrana yazılması
            global lblSonuc
            if seciliYontem == "Dikdörtgen Kuralı" :
                lblSonuc = QLabel(" ∫ = "+str(self.DikdortgenKurali(seciliFonksiyon,a,b,adimSayisi)),self)
            elif seciliYontem == "Orta Dikdörtgen Kuralı" :
                lblSonuc = QLabel(" ∫ = "+str(self.OrtaDikdortgenKurali(seciliFonksiyon,a,b,adimSayisi)),self) 
            elif seciliYontem == "Yamuk Kuralı" :
                lblSonuc = QLabel(" ∫ = "+str(self.YamukKurali(seciliFonksiyon,a,b,adimSayisi)),self) 
            elif seciliYontem == "Simpson Kuralı" :
                lblSonuc = QLabel(" ∫ = "+str(self.SimpsonKurali(seciliFonksiyon,a,b,adimSayisi)),self) 
            lblSonuc.setFont(QFont("Comic Sans MS",18))
            lblSonuc.setStyleSheet("color :#FF00BF")
            lblSonuc.setGeometry(550,150,20000,100)
            lblSonuc.show()
    
    def Temizle(self,lnEdtA,lnEdtB,lnEdtAdim,prgBrIslem):
        # Kutuları Temizleme
        lnEdtA.clear()
        lnEdtB.clear()
        lnEdtAdim.clear()
        prgBrIslem.reset()
        lblSonuc.clear()
        lblSonucTanim.clear()

    def DikdortgenKurali(self,fonksiyon,a,b,adimSayisi):
        aralikFark = abs(float(a)-float(b))
        fark = aralikFark/float(adimSayisi)
        integral = 0
        for i in self.Aralik(float(a)+fark,float(b)+fark,fark):
            if fonksiyon == "(13(x-x^(2)))/√(e^3x )" : 
                fx = (13*(i-pow(i,2)))/(math.sqrt(math.exp(3*i)))
            elif fonksiyon == "e^x" :
                fx = math.exp(i)
            elif fonksiyon == "x*sinx" : 
                fx = i * math.sin(i)
            elif fonksiyon == "(x^2)+4" : 
                fx = (pow(i,2)+4)
            elif fonksiyon == "4/(1+x^2)" : 
                fx = (4/(1+(pow(i,2))))

            alanx= fx * fark
            integral += alanx
            self.prgBrIslem.setMaximum(float(b)) # islem durumunu progress barda göstermek için max ayarı
            self.prgBrIslem.setValue(i) # islem durumunu progress barda gösterme
        return abs(integral)
    
    def OrtaDikdortgenKurali(self,fonksiyon,a,b,adimSayisi):
        aralikFark = abs(float(a)-float(b))
        fark = aralikFark/float(adimSayisi)
        integral = 0
        for i in self.Aralik(float(a)+fark,float(b)+fark,fark):
            if fonksiyon == "(13(x-x^(2)))/√(e^3x )" : 
                fx = (13*((i-(fark/2))-pow((i-(fark/2)),2)))/(math.sqrt(math.exp(3*(i-(fark/2)))))
            elif fonksiyon == "e^x" :
                fx = math.exp((i-(fark/2)))
            elif fonksiyon == "x*sinx" : 
                fx = (i-(fark/2)) * math.sin((i-(fark/2)))
            elif fonksiyon == "(x^2)+4" : 
                fx = (pow((i-(fark/2)),2)+4)
            elif fonksiyon == "4/(1+x^2)" : 
                fx = (4/(1+(pow((i-(fark/2)),2))))
            alanx= fx * fark
            integral += alanx
            self.prgBrIslem.setMaximum(float(b))
            self.prgBrIslem.setValue(i)
        return abs(integral)

    def YamukKurali(self,fonksiyon,a,b,adimSayisi):
        aralikFark = abs(float(a)-float(b))
        fark = aralikFark/float(adimSayisi)
        integral = 0
        toplamFx=fx=fxa=fxb= 0
        for i in self.Aralik(float(a)+fark,float(b),fark):
            if fonksiyon == "(13(x-x^(2)))/√(e^3x )" :
                    fxa= (13*(float(a)-pow(float(a),2)))/(math.sqrt(math.exp(3*float(a))))
                    fxb= (13*(float(b)-pow(float(b),2)))/(math.sqrt(math.exp(3*float(b))))
                    fx = (13*(i-pow(i,2)))/(math.sqrt(math.exp(3*i)))
                    print(i)
            elif fonksiyon == "e^x":
                    fxa = math.exp(float(a))
                    fxb = math.exp(float(b))
                    fx = math.exp(i)
            elif fonksiyon == "x*sinx" : 
                    fxa = i * math.sin(float(a))
                    fxb = i * math.sin(float(b))
                    fx = i * math.sin(i)
            elif fonksiyon == "(x^2)+4" :
                    fxa = (pow(float(a),2)+4)
                    fxb = (pow(float(b),2)+4)
                    fx = (pow(i,2)+4)
            elif fonksiyon == "4/(1+x^2)" : 
                    fxa = (4/(1+(pow(float(a),2))))
                    fxb = (4/(1+(pow(float(b),2))))
                    fx = (4/(1+(pow(i,2))))
            toplamFx += fx
            integral = (fxa+fxb+(2*toplamFx))*(fark/2) 
        return abs(integral)

    def SimpsonKurali(self,fonksiyon,a,b,adimSayisi):
        aralikFark = abs(float(a)-float(b))
        fark = aralikFark/float(adimSayisi)
        integral = 0
        toplamTekFx=toplamCiftFx=fx=fxa=fxb= 0
        for i in self.Aralik(float(a)+fark,float(b),fark):
            if fonksiyon == "(13(x-x^(2)))/√(e^3x )" :
                    fxa= (13*(float(a)-pow(float(a),2)))/(math.sqrt(math.exp(3*float(a))))
                    fxb= (13*(float(b)-pow(float(b),2)))/(math.sqrt(math.exp(3*float(b))))
                    if(i%2==0):
                        fx = (13*(i-pow(i,2)))/(math.sqrt(math.exp(3*i)))
                        toplamCiftFx += fx
                    else:
                        fx = (13*(i-pow(i,2)))/(math.sqrt(math.exp(3*i)))
                        toplamTekFx += fx
            elif fonksiyon == "e^x":
                    fxa = math.exp(float(a))
                    fxb = math.exp(float(b))
                    if(i%2==0):
                        fx = math.exp(i)
                        toplamCiftFx += fx
                    else:
                        fx = math.exp(i)
                        toplamTekFx += fx
            elif fonksiyon == "x*sinx" : 
                    fxa = i * math.sin(float(a))
                    fxb = i * math.sin(float(b))
                    if(i%2==0):
                        fx = i * math.sin(i)
                        toplamCiftFx += fx
                    else:
                        fx = i * math.sin(i)
                        toplamTekFx += fx
            elif fonksiyon == "(x^2)+4" :
                    fxa = (pow(float(a),2)+4)
                    fxb = (pow(float(b),2)+4)
                    if(i%2==0):
                        fx = (pow(i,2)+4)
                        toplamCiftFx += fx
                    else:
                        fx = (pow(i,2)+4)
                        toplamTekFx += fx
            elif fonksiyon == "4/(1+x^2)" : 
                    fxa = (4/(1+(pow(float(a),2))))
                    fxb = (4/(1+(pow(float(b),2))))
                    if(i%2==0):
                        fx = (4/(1+(pow(i,2))))
                        toplamCiftFx += fx
                    else:
                        fx = (4/(1+(pow(i,2))))
                        toplamTekFx += fx
            integral = (fxa+fxb+(4*toplamTekFx)+(2*toplamCiftFx))*(fark/3) 
        return abs(integral)

    # Alınan ilk değeri son değere kadar verilen arış miktarına göre artıran metot
    def Aralik(self,ilkDeger,sonDeger,artis):
        i = ilkDeger
        while i < sonDeger:
            yield i
            i += artis  
        
def Main():    
    app = QApplication(sys.argv) # Uygulama oluşturma
    GUI = Pencere() # Pencere oluşturma
    sys.exit(app.exec_())# Kapatma

Main()