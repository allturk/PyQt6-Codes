from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def btnClicked(self):
        print("Button Clicked")

    def initUI(self):
        self.setGeometry(410, 290, 700, 400)
        self.setWindowTitle('Python Gui Development')
        self.setWindowIcon(QIcon("../images/computer.png"))

        self.setStyleSheet("background-color: lightblue")
        self.create_button()


    def create_button(self):
        btn = QPushButton('Click Me', self)
        btn.setGeometry(100, 100, 100, 40)
        btn.setFont(QFont('Arial', 12, QFont.Weight.Bold, True))
        btn.setIcon(QIcon("../images/java.png"))
        btn.setIconSize(QSize(20, 20))
        btn.clicked.connect(self.btnClicked)

app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())
