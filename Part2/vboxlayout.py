from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('PyQt6 Study')
        self.setWindowIcon(QIcon('../images/computer.png'))
        vbox = QVBoxLayout()
        btn1 = QPushButton('Click 1', self)
        btn2 = QPushButton('Click 2', self)
        btn3 = QPushButton('Click 3', self)
        btn4 = QPushButton('Click 4', self)
        vbox.addStretch()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        self.setLayout(vbox)
        btn1.clicked.connect(lambda: self.btn_clicked('1'))
        btn2.clicked.connect(lambda: self.btn_clicked(event='2'))
        btn3.clicked.connect(lambda: self.btn_clicked(event='3'))
        btn4.clicked.connect(lambda: self.btn_clicked(event='4'))
        # vbox.addSpacing(100) #alttan 100px boşluk bırakır
        vbox.addStretch()
    def btn_clicked(self, event):
        if event == "1":
            print('Btn1 Clicked')
        elif event == "2":
            print('Btn2 Clicked')
        elif event == "3":
            print('Btn3 Clicked')
        elif event == "4":
            print('Btn4 Clicked')

app= QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())