from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTime, QTimer
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(410, 290, 700, 400)
        self.setWindowTitle('PyQt6 QLCDNumber Clock')
        self.setWindowIcon(QIcon("../images/computer.png"))
        self.create_combo()


    def create_combo(self):
        hbox=QHBoxLayout()

        label=QLabel("Select Account Type: ")
        label.setFont(QFont("Times",15))

        self.combo=QComboBox()
        self.combo.addItem("Current Account")
        self.combo.addItem("Deposit Account")
        self.combo.addItem("Saving Account")
        self.combo.currentTextChanged.connect(self.combo_changed)

        vbox=QVBoxLayout()
        self.label_result=QLabel("Hello")
        self.label_result.setFont(QFont("Times",15))
        vbox.addLayout(hbox)
        vbox.addWidget(self.label_result)
        hbox.addWidget(label)
        hbox.addWidget(self.combo)

        self.setLayout(vbox)

    def combo_changed(self):
        item=self.combo.currentText()
        self.label_result.setText(f"Your account is now {item}")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
