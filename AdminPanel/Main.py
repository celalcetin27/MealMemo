# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from  login_k import loginpage
app = QApplication([])
pencere = loginpage()
pencere.show()
app.exec_()
