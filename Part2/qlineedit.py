from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('PyQt6')
        self.setWindowIcon(QIcon('../images/computer.png'))

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setFont(QFont('SansSerif', 12))
        # self.lineEdit.setText("Default Text")
        self.lineEdit.setPlaceholderText("Enter your text here")
        # self.lineEdit.setEnabled(False)
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        # self.lineEdit.move(20, 20)
        # self.lineEdit.resize(250, 40)

        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
