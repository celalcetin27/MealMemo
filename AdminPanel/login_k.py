# -- coding: utf-8 --
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from login import Ui_Form
from Anapencere_k import AnapencerePage
import mysql.connector
# from config import *

class loginpage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.loginform.pushButton_giris.clicked.connect(self.girisyap)
        self.anapencereaç = AnapencerePage()
        
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': '22982591604',
            'database': 'mealmemo'
        }
        
        self.baglanti = mysql.connector.connect(**config)
        self.cursor = self.baglanti.cursor()

    def girisyap(self):
        email = self.loginform.lineEdit_gmail.text()
        password = self.loginform.lineEdit_sifre.text()
        
        query = "SELECT * FROM admin_list WHERE user_email = %s AND user_password = %s"
        self.cursor.execute(query, (email, password))
        user = self.cursor.fetchone()

        if user:
            print("Giriş Başarılı")  # Giriş başarılı olduğunda yapılacak işlemleri burada yapabilirsiniz
            self.anapencereaç.show()  # Giriş başarılıysa yeni pencereyi göster
            self.close()  # Giriş penceresini kapat
        else:
            self.loginform.label_kontrol.setText("Kullanıcı Gmaili veya Şifre Yanlış!!")
    
    def closeEvent(self, event):
        if self.baglanti.is_connected():
            self.baglanti.close()
            print("Veritabanı bağlantısı kapatıldı")
