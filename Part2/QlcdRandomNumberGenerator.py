import random

from PyQt6.QtWidgets import QApplication, QDialog, QPushButton,QLCDNumber
from PyQt6 import uic
import sys
import secrets


class UI(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi("QLCDRNGenratorDemo.ui", self)
        self.rnd_generate=self.findChild(QPushButton,"btn_generate")
        self.lcd=self.findChild(QLCDNumber,"lcdNumber")
        self.lcd.setDigitCount(20)

        self.rnd_generate.clicked.connect(self.generate_number)


    def generate_number(self):
        number=secrets.token_hex(10)
        print(number)
        self.lcd.display(number)



app=QApplication([])
window=UI()
window.show()
sys.exit(app.exec())