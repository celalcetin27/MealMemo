# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Ui_Form(object):
    def setupUi(self, Form):
        font = QFont()
        font.setPointSize(20)
        Form.setObjectName("Form")
        Form.resize(298, 344)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setFont(font)  
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_gmail = QtWidgets.QLineEdit(Form)
        self.lineEdit_gmail.setObjectName("lineEdit_gmail")
        self.verticalLayout.addWidget(self.lineEdit_gmail)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)  
        self.label.setFont(font) 
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_sifre = QtWidgets.QLineEdit(Form)
        self.lineEdit_sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_sifre.setObjectName("lineEdit_sifre")
        self.verticalLayout.addWidget(self.lineEdit_sifre)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label_kontrol = QtWidgets.QLabel(Form)
        self.label_kontrol.setObjectName("label_kontrol")
        self.verticalLayout.addWidget(self.label_kontrol)
        self.label_kontrol.setAlignment(Qt.AlignCenter)  
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton_giris = QtWidgets.QPushButton(Form)
        self.pushButton_giris.setObjectName("pushButton_giris")
        self.pushButton_giris.setFont(font) 
        self.verticalLayout.addWidget(self.pushButton_giris)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Gmail"))
        self.label.setText(_translate("Form", "Şifre"))
        self.label_kontrol.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_kontrol.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_giris.setText(_translate("Form", "Giriş"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())