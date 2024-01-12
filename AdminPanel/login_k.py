# -- coding: utf-8 --
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from login import Ui_Form
from Anapencere_k import AnapencerePage
# from config import *

class loginpage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.loginform.pushButton_giris.clicked.connect(self.girisyap)
        self.anapencereaç = AnapencerePage()
        

    def girisyap(self):
        email = self.loginform.lineEdit_gmail.text()
        password = self.loginform.lineEdit_sifre.text()
        
        if email=="admin@gmail.com" and password=="123456":
            self.anapencereaç.show()  # Giriş başarılıysa yeni pencereyi göster
            self.close()  # Giriş penceresini kapat
        else:
            self.loginform.label_kontrol.setText("Kullanıcı Gmaili veya Şifre Yanlış!!")

    
