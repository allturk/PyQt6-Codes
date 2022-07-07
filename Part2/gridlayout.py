from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('PyQt6 Study')
        self.setWindowIcon(QIcon('../images/computer.png'))
        grid = QGridLayout()
        btn1 = QPushButton('Click 1', self)
        btn2 = QPushButton('Click 2', self)
        btn3 = QPushButton('Click 3', self)
        btn4 = QPushButton('Click 4', self)
        btn5 = QPushButton('Click 5', self)
        btn6 = QPushButton('Click 6', self)
        btn7 = QPushButton('Click 7', self)
        btn8 = QPushButton('Click 8', self)
        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)
        self.setLayout(grid)
        btn1.clicked.connect(lambda: self.btn_clicked('1'))
        btn2.clicked.connect(lambda: self.btn_clicked(event='2'))
        btn3.clicked.connect(lambda: self.btn_clicked(event='3'))
        btn4.clicked.connect(lambda: self.btn_clicked(event='4'))
        btn5.clicked.connect(lambda: self.btn_clicked(event='5'))
        btn6.clicked.connect(lambda: self.btn_clicked(event='6'))
        btn7.clicked.connect(lambda: self.btn_clicked(event='7'))
        btn8.clicked.connect(lambda: self.btn_clicked(event='8'))
        self.setLayout(grid)

    def btn_clicked(self, event):
        if event == "1":
            print('Btn1 Clicked')
        elif event == "2":
            print('Btn2 Clicked')
        elif event == "3":
            print('Btn3 Clicked')
        elif event == "4":
            print('Btn4 Clicked')
        elif event == "5":
            print('Btn5 Clicked')
        elif event == "6":
            print('Btn6 Clicked')
        elif event == "7":
            print('Btn7 Clicked')
        elif event == "8":
            print('Btn8 Clicked')



app = QApplication(sys.argv)
window = Windows()
window.show()
sys.exit(app.exec())
