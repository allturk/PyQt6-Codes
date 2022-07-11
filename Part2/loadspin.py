from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QDoubleSpinBox
from PyQt6 import uic
import sys


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("DoubleSpinDemo.ui", self)
        self.linePrice = self.findChild(QLineEdit, "ledit_price")
        self.dspin = self.findChild(QDoubleSpinBox, "dspinbox")
        self.dspin.valueChanged.connect(self.spin_selected)
        self.lineTotal = self.findChild(QLineEdit, "ledit_total")

    def spin_selected(self):
        if self.linePrice.text() != "0":
            price = int(self.linePrice.text())
            totalprice = self.dspin.value() * price
            self.lineTotal.setText(str(totalprice))


app = QApplication(sys.argv)
windowui = UI()
windowui.show()
sys.exit(app.exec())
