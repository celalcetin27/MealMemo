# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from kullanıcılistele import Ui_Form

class kullanıcılistelepage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.kullanıcılistelepage=Ui_Form()
        self.kullanıcılistelepage.setupUi(self)
