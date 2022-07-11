from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTime, QTimer
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(410, 290, 700, 400)
        self.setWindowTitle('PyQt6 QLCDNumber Clock')
        self.setWindowIcon(QIcon("../images/computer.png"))
        # self.setFixedHeight(400)
        # self.setFixedWidth(700)
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(8)
        self.lcd.setStyleSheet("font-size:50")
        self.setStyleSheet("background-color: lightblue")
        self.timer = QTimer()
        self.timer.timeout.connect(self.showLCD)
        self.timer.start(1000)
        # self.showLCD()
        # self.setWindowOpacity(0.9)

    def showLCD(self):
        vbox = QVBoxLayout()

        self.lcd.setStyleSheet('background:red')

        vbox.addWidget(self.lcd)
        self.time = QTime.currentTime()
        self.text = self.time.toString("hh:mm:ss")
        # if (self.time.second() % 2) == 0:
        #     self.text = self.text[:2] + ' ' + self.text[3:]

        self.lcd.display(self.text)
        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
