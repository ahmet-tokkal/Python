# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tasarim.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(999, 439)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(138, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 8, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Form.setPalette(palette)
        Form.setFocusPolicy(QtCore.Qt.TabFocus)
        Form.setStyleSheet("color:#8A0808")
        self.lblFonksiyon = QtWidgets.QLabel(Form)
        self.lblFonksiyon.setGeometry(QtCore.QRect(15, 100, 201, 38))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lblFonksiyon.setFont(font)
        self.lblFonksiyon.setStyleSheet("color:#FFFF00")
        self.lblFonksiyon.setObjectName("lblFonksiyon")
        self.cmbBoxYontem = QtWidgets.QComboBox(Form)
        self.cmbBoxYontem.setGeometry(QtCore.QRect(210, 170, 261, 38))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.cmbBoxYontem.setFont(font)
        self.cmbBoxYontem.setStyleSheet("background-color:#F7F2E0;color:black")
        self.cmbBoxYontem.setObjectName("cmbBoxYontem")
        self.cmbBoxYontem.addItem("")
        self.cmbBoxYontem.addItem("")
        self.lblYontem = QtWidgets.QLabel(Form)
        self.lblYontem.setGeometry(QtCore.QRect(40, 170, 178, 38))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lblYontem.setFont(font)
        self.lblYontem.setStyleSheet("color:#FFFF00")
        self.lblYontem.setObjectName("lblYontem")
        self.cmbBxFonksiyon = QtWidgets.QComboBox(Form)
        self.cmbBxFonksiyon.setGeometry(QtCore.QRect(210, 100, 261, 38))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.cmbBxFonksiyon.setFont(font)
        self.cmbBxFonksiyon.setStyleSheet("background-color:#F7F2E0; color:black")
        self.cmbBxFonksiyon.setObjectName("cmbBxFonksiyon")
        self.cmbBxFonksiyon.addItem("")
        self.lblAdimSayisi = QtWidgets.QLabel(Form)
        self.lblAdimSayisi.setGeometry(QtCore.QRect(40, 290, 178, 38))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lblAdimSayisi.setFont(font)
        self.lblAdimSayisi.setStyleSheet("color:#FFFF00")
        self.lblAdimSayisi.setObjectName("lblAdimSayisi")
        self.lblA = QtWidgets.QLabel(Form)
        self.lblA.setGeometry(QtCore.QRect(163, 230, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lblA.setFont(font)
        self.lblA.setStyleSheet("color:#FFFF00")
        self.lblA.setObjectName("lblA")
        self.lblB = QtWidgets.QLabel(Form)
        self.lblB.setGeometry(QtCore.QRect(320, 230, 38, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lblB.setFont(font)
        self.lblB.setStyleSheet("color:#FFFF00")
        self.lblB.setObjectName("lblB")
        self.lnEdtA = QtWidgets.QLineEdit(Form)
        self.lnEdtA.setGeometry(QtCore.QRect(210, 230, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.lnEdtA.setFont(font)
        self.lnEdtA.setStyleSheet("color:black")
        self.lnEdtA.setObjectName("lnEdtA")
        self.lnEdtB = QtWidgets.QLineEdit(Form)
        self.lnEdtB.setGeometry(QtCore.QRect(360, 230, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.lnEdtB.setFont(font)
        self.lnEdtB.setStyleSheet("color:black")
        self.lnEdtB.setObjectName("lnEdtB")
        self.lnEdtAdimSayisi = QtWidgets.QLineEdit(Form)
        self.lnEdtAdimSayisi.setGeometry(QtCore.QRect(210, 290, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.lnEdtAdimSayisi.setFont(font)
        self.lnEdtAdimSayisi.setStyleSheet("color:black")
        self.lnEdtAdimSayisi.setObjectName("lnEdtAdimSayisi")
        self.btnHesapla = QtWidgets.QPushButton(Form)
        self.btnHesapla.setGeometry(QtCore.QRect(150, 350, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnHesapla.setFont(font)
        self.btnHesapla.setStyleSheet("background-color:#FE2E64; color:white")
        self.btnHesapla.setObjectName("btnHesapla")
        self.btnTemizle = QtWidgets.QPushButton(Form)
        self.btnTemizle.setGeometry(QtCore.QRect(300, 350, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnTemizle.setFont(font)
        self.btnTemizle.setStyleSheet("background-color:#4000FF; color:white")
        self.btnTemizle.setObjectName("btnTemizle")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(210, 20, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lcdSonuc = QtWidgets.QLCDNumber(Form)
        self.lcdSonuc.setGeometry(QtCore.QRect(670, 280, 291, 51))
        self.lcdSonuc.setObjectName("lcdSonuc")
        self.lblTanim = QtWidgets.QLabel(Form)
        self.lblTanim.setGeometry(QtCore.QRect(530, 100, 201, 38))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lblTanim.setFont(font)
        self.lblTanim.setStyleSheet("color:#FFFF00")
        self.lblTanim.setText("")
        self.lblTanim.setObjectName("lblTanim")
        self.lblSonuc = QtWidgets.QLabel(Form)
        self.lblSonuc.setGeometry(QtCore.QRect(540, 290, 131, 38))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lblSonuc.setFont(font)
        self.lblSonuc.setStyleSheet("color:#FFFF00")
        self.lblSonuc.setObjectName("lblSonuc")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblFonksiyon.setText(_translate("Form", "Fonksiyon Seç :"))
        self.cmbBoxYontem.setItemText(0, _translate("Form", "Fixed Point"))
        self.cmbBoxYontem.setItemText(1, _translate("Form", "Bisection"))
        self.lblYontem.setText(_translate("Form", "Yöntem Seç :"))
        self.cmbBxFonksiyon.setItemText(0, _translate("Form", "  x^3 + 3x - 20 = 0"))
        self.lblAdimSayisi.setText(_translate("Form", "Adım Sayısı :"))
        self.lblA.setText(_translate("Form", "A :"))
        self.lblB.setText(_translate("Form", "B :"))
        self.btnHesapla.setText(_translate("Form", "Hesapla"))
        self.btnTemizle.setText(_translate("Form", "Temizle"))
        self.label_6.setText(_translate("Form", "Lineer Olmayan Denlemlerin Köklerini Bulma"))
        self.lblSonuc.setText(_translate("Form", "Sonuç = "))

