import time

from PyQt6.QtCore import QSize, QEvent
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QHBoxLayout,QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(410, 290, 300, 200)
        self.setWindowTitle("PyQt6 QRadioButton")
        self.setWindowIcon(QIcon("../images/computer.png"))
        self.create_radio()

    def create_radio(self):
        radiobtn = QRadioButton("Python")
        radiobtn.setIcon(QIcon("../images/python.png"))
        radiobtn.setIconSize(QSize(20, 20))
        radiobtn.setFont(QFont("Times", 14))
        # radiobtn.setChecked(True)
        radiobtn.toggled.connect(self.radio_selected)

        radiobtn2=QRadioButton("Java")
        radiobtn2.setIcon(QIcon("../images/java.png"))
        radiobtn2.setIconSize(QSize(20,20))
        radiobtn2.setFont(QFont("Times",14))
        radiobtn2.toggled.connect(self.radio_selected)

        radiobtn3 = QRadioButton("JavaScript")
        radiobtn3.setIcon(QIcon("../images/javascript.png"))
        radiobtn3.setIconSize(QSize(20, 20))
        radiobtn3.setFont(QFont("Times", 14))
        radiobtn3.toggled.connect(self.radio_selected)
        self.label=QLabel("")
        self.label.setFont(QFont("Sanserif",15))

        hbox = QHBoxLayout()
        vbox=QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        hbox.addWidget(radiobtn)
        hbox.addWidget(radiobtn2)
        hbox.addWidget(radiobtn3)
        self.setLayout(vbox)

    def radio_selected(self):
        radio_btn=self.sender()
        rad_text = radio_btn.text()
        if radio_btn.isChecked():
            self.label.setText(f"You have selected: {rad_text}")



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
