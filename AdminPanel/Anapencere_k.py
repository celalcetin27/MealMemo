# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from Anapencere import Ui_MainWindow
from kullanıcılistele_k import kullanıcılistelepage
from Yemekdatasi_k import Yemekdatapage
from botlarım import *
 
class AnapencerePage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.anapencereform=Ui_MainWindow()
        self.anapencereform.setupUi(self)
        self.kullanac= kullanıcılistelepage()
        self.yemekac= Yemekdatapage()
        self.anapencereform.actionKullan_c_Datalar.triggered.connect(self.urunngit)
        self.anapencereform.actionYemek_Datalar.triggered.connect(self.yemekgit)
        self.anapencereform.pushButton_Datacek.clicked.connect(self.bas)
        
    def bas(self):
        if self.anapencereform.radioButton_Alamy.isChecked():
            if self.anapencereform.radioButton_5.isChecked():
                alamy(self.anapencereform.lineEdit_nedata.text(),5)
            elif self.anapencereform.radioButton_10.isChecked():
                alamy(self.anapencereform.lineEdit_nedata.text(),10)
            elif self.anapencereform.radioButton_15.isChecked():
                alamy(self.anapencereform.lineEdit_nedata.text(),15)
            elif self.anapencereform.radioButton_20.isChecked():
                alamy(self.anapencereform.lineEdit_nedata.text(),20)
            elif self.anapencereform.radioButton_25.isChecked():
                alamy(self.anapencereform.lineEdit_nedata.text(),25)
            elif self.anapencereform.radioButton_30.isChecked():
                alamy(self.anapencereform.lineEdit_nedata.text(),30)
            elif self.anapencereform.radioButton_35.isChecked():
                alamy(self.anapencereform.lineEdit_nedata.text(),35)
            
        elif self.anapencereform.radioButton_Google.isChecked():
            if self.anapencereform.radioButton_5.isChecked():
                google(self.anapencereform.lineEdit_nedata.text(),5)
            elif self.anapencereform.radioButton_10.isChecked():
                google(self.anapencereform.lineEdit_nedata.text(),10)
            elif self.anapencereform.radioButton_15.isChecked():
                google(self.anapencereform.lineEdit_nedata.text(),15)
            elif self.anapencereform.radioButton_20.isChecked():
                google(self.anapencereform.lineEdit_nedata.text(),20)
            elif self.anapencereform.radioButton_25.isChecked():
                google(self.anapencereform.lineEdit_nedata.text(),25)
            elif self.anapencereform.radioButton_30.isChecked():
                google(self.anapencereform.lineEdit_nedata.text(),30)
            elif self.anapencereform.radioButton_35.isChecked():
                google(self.anapencereform.lineEdit_nedata.text(),35)
                
        elif self.anapencereform.radioButton_123RF.isChecked():
            if self.anapencereform.radioButton_5.isChecked():
                onetwothreerf(self.anapencereform.lineEdit_nedata.text(),5)
            elif self.anapencereform.radioButton_10.isChecked():
                onetwothreerf(self.anapencereform.lineEdit_nedata.text(),10)
            elif self.anapencereform.radioButton_15.isChecked():
                onetwothreerf(self.anapencereform.lineEdit_nedata.text(),15)
            elif self.anapencereform.radioButton_20.isChecked():
                onetwothreerf(self.anapencereform.lineEdit_nedata.text(),20)
            elif self.anapencereform.radioButton_25.isChecked():
                onetwothreerf(self.anapencereform.lineEdit_nedata.text(),25)
            elif self.anapencereform.radioButton_30.isChecked():
                onetwothreerf(self.anapencereform.lineEdit_nedata.text(),30)
            elif self.anapencereform.radioButton_35.isChecked():
                onetwothreerf(self.anapencereform.lineEdit_nedata.text(),35)
        elif self.anapencereform.radioButton_Freepik.isChecked():
            if self.anapencereform.radioButton_5.isChecked():
                freepik(self.anapencereform.lineEdit_nedata.text(),5)
            elif self.anapencereform.radioButton_10.isChecked():
                freepik(self.anapencereform.lineEdit_nedata.text(),10)
            elif self.anapencereform.radioButton_15.isChecked():
                freepik(self.anapencereform.lineEdit_nedata.text(),15)
            elif self.anapencereform.radioButton_20.isChecked():
                freepik(self.anapencereform.lineEdit_nedata.text(),20)
            elif self.anapencereform.radioButton_25.isChecked():
                freepik(self.anapencereform.lineEdit_nedata.text(),25)
            elif self.anapencereform.radioButton_30.isChecked():
                freepik(self.anapencereform.lineEdit_nedata.text(),30)
            elif self.anapencereform.radioButton_35.isChecked():
                freepik(self.anapencereform.lineEdit_nedata.text(),35)
        elif self.anapencereform.radioButton_Shutterstock.isChecked():
            if self.anapencereform.radioButton_5.isChecked():
                shutterstock(self.anapencereform.lineEdit_nedata.text(),5)
            elif self.anapencereform.radioButton_10.isChecked():
                shutterstock(self.anapencereform.lineEdit_nedata.text(),10)
            elif self.anapencereform.radioButton_15.isChecked():
                shutterstock(self.anapencereform.lineEdit_nedata.text(),15)
            elif self.anapencereform.radioButton_20.isChecked():
                shutterstock(self.anapencereform.lineEdit_nedata.text(),20)
            elif self.anapencereform.radioButton_25.isChecked():
                shutterstock(self.anapencereform.lineEdit_nedata.text(),25)
            elif self.anapencereform.radioButton_30.isChecked():
                shutterstock(self.anapencereform.lineEdit_nedata.text(),30)
            elif self.anapencereform.radioButton_35.isChecked():
                shutterstock(self.anapencereform.lineEdit_nedata.text(),35)
        elif self.anapencereform.radioButton_Pexels.isChecked():
            if self.anapencereform.radioButton_5.isChecked():
                pexels(self.anapencereform.lineEdit_nedata.text(),5)
            elif self.anapencereform.radioButton_10.isChecked():
                pexels(self.anapencereform.lineEdit_nedata.text(),10)
            elif self.anapencereform.radioButton_15.isChecked():
                pexels(self.anapencereform.lineEdit_nedata.text(),15)
            elif self.anapencereform.radioButton_20.isChecked():
                pexels(self.anapencereform.lineEdit_nedata.text(),20)
            elif self.anapencereform.radioButton_25.isChecked():
                pexels(self.anapencereform.lineEdit_nedata.text(),25)
            elif self.anapencereform.radioButton_30.isChecked():
                pexels(self.anapencereform.lineEdit_nedata.text(),30)
            elif self.anapencereform.radioButton_35.isChecked():
                pexels(self.anapencereform.lineEdit_nedata.text(),35)
        elif self.anapencereform.radioButton_Pikwizard.isChecked():
            if self.anapencereform.radioButton_5.isChecked():
                (self.anapencereform.lineEdit_nedata.text(),5)
            elif self.anapencereform.radioButton_10.isChecked():
                Pikwizard(self.anapencereform.lineEdit_nedata.text(),10)
            elif self.anapencereform.radioButton_15.isChecked():
                Pikwizard(self.anapencereform.lineEdit_nedata.text(),15)
            elif self.anapencereform.radioButton_20.isChecked():
                Pikwizard(self.anapencereform.lineEdit_nedata.text(),20)
            elif self.anapencereform.radioButton_25.isChecked():
                Pikwizard(self.anapencereform.lineEdit_nedata.text(),25)
            elif self.anapencereform.radioButton_30.isChecked():
                Pikwizard(self.anapencereform.lineEdit_nedata.text(),30)
            elif self.anapencereform.radioButton_35.isChecked():
                Pikwizard(self.anapencereform.lineEdit_nedata.text(),35)
        else:
            print("Geçersiz")


    def urunngit(self):
        self.kullanac.show()
    
    def yemekgit(self):
        self.yemekac.show()