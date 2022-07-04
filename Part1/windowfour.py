from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(410, 290, 700, 400)
        self.setWindowTitle('Python Gui Development')
        self.setWindowIcon(QIcon("../images/computer.png"))
        # self.setFixedHeight(400)
        # self.setFixedWidth(700)

        self.setStyleSheet("background-color: lightblue")
        # self.setWindowOpacity(0.9)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
