from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import os
from Yemekdatasi import Ui_Form

class Yemekdatapage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.Yemekdatapage_e = Ui_Form()
        self.Yemekdatapage_e.setupUi(self)
        self.Yemekdatapage_e.comboBox_hangisite.currentIndexChanged.connect(self.selection_changed)
        self.Yemekdatapage_e.lineEdit_yemek.textChanged.connect(self.resimisimgetir)
        self.Yemekdatapage_e.pushButton.clicked.connect(self.resimgetir)
        self.Yemekdatapage_e.pushButton_4.clicked.connect(self.silme)
        self.Yemekdatapage_e.pushButton_2.clicked.connect(self.hepsinisilme)

        # QScrollArea ekle
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)

        self.Yemekdatapage_e.verticalLayout.addWidget(self.scroll_area)

    def selection_changed(self, index):
        self.selected_text = self.Yemekdatapage_e.comboBox_hangisite.currentText()
    def resimisimgetir(self):
        self.yemekismi = self.Yemekdatapage_e.lineEdit_yemek.text()
    def silme(self):
        layout = self.scroll_layout
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clearLayout(child.layout())
    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clearLayout(child.layout())
    def resimgetir(self):
        row_layout = QHBoxLayout()  # Yeni bir QHBoxLayout oluşturun
        self.yemekismi=self.yemekismi.lower().replace(" ",".")
        
        a=self.selected_text+"_"+self.yemekismi
        b=self.yemekismi
        if os.path.exists(a):
            self.Yemekdatapage_e.label_hata.setText("")
            dosya_listesi = os.listdir(a)
            dosya_sayisi = len(dosya_listesi)
        
            for i in range(1, (dosya_sayisi+1)):
                
                image_path = f"{a}/{b}{i}.jpg"  # Resimlerin yolunu belirtin (örneğin, resim1.jpg, resim2.jpg, ...)

                if os.path.exists(image_path):
                    pixmap = QPixmap(image_path)
                    pixmap = pixmap.scaled(100, 100)  # Resmin boyutunu ayarlayabilirsiniz

                    label = QLabel()
                    label.setPixmap(pixmap)
                    label.setScaledContents(True)

                    image_widget = QWidget()
                    layout = QVBoxLayout(image_widget)
                    layout.addWidget(label)

                    row_layout.addWidget(image_widget)  # Resmi satır düzenine ekleyin

                    # Eğer 5 resim eklendiyse yeni bir satır oluşturun
                    if i % 5 == 0:
                        self.scroll_layout.addLayout(row_layout)
                        row_layout = QHBoxLayout()  # Yeni bir satır için yeni bir QHBoxLayout oluşturun
                                            
                else:
                    self.Yemekdatapage_e.label_hata.setText("Siteye ait Resim Datası Bulunamadı!!")
                    
        else:
            self.Yemekdatapage_e.label_hata.setText("Siteye ait Resim Datası Bulunamadı!!")
        # Son kalan resimleri ekleyin (5 resmin tamamlayıcı olmayacağı durumlar için)
        if row_layout.count() > 0:
            self.scroll_layout.addLayout(row_layout)


    def hepsinisilme(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setText("Emin misiniz?")
        msg_box.setInformativeText("Bu işlem geri alınamaz.")
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        result = msg_box.exec_()

        if result == QMessageBox.Ok:
            layout = self.scroll_layout
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                elif child.layout():
                    self.clearLayout(child.layout())

           
            a = self.selected_text + "_" + self.yemekismi
            if os.path.exists(a):
                import shutil
                shutil.rmtree(a)
                self.Yemekdatapage_e.label_hata.setText("")
            else:
                self.Yemekdatapage_e.label_hata.setText("Siteye ait Resim Datası Bulunamadı!!")
        #while layout.count():
            #child = layout.takeAt(0)
            #if child.widget():
               # child.widget().deleteLater()
            #elif child.layout():
                #self.clearLayout(child.layout())