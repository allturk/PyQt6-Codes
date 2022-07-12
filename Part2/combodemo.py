from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel
from PyQt6 import uic
import sys


class UIDemo(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("comboboxdemo.ui", self)
        self.combo = self.findChild(QComboBox, "combo")
        self.label = self.findChild(QLabel, "lbl_result")
        self.combo.currentTextChanged.connect(self.combo_selected)

    def combo_selected(self):
        text = self.combo.currentText()
        self.label.setText(f"Your favourite language is {text}")


app = QApplication([])
windowui = UIDemo()
windowui.show()
sys.exit(app.exec())
