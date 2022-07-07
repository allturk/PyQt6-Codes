from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton,QLabel
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('PyQt6 Event Handling')
        self.setWindowIcon(QIcon('../images/computer.png'))
        self.create_widget()

    def create_widget(self):

        hbox = QHBoxLayout()
        btn1 = QPushButton('Change Text')
        btn1.clicked.connect(self.clicked_btn)
        self.lbl=QLabel('Text will be shown here')

        hbox.addStretch()
        hbox.addWidget(btn1)
        hbox.addWidget(self.lbl)
        hbox.addStretch()
        self.setLayout(hbox)


    def clicked_btn(self):
        self.lbl.setText('Button Clicked')
        self.lbl.setFont(QFont('Times', 12, QFont.Weight.Bold,False))
        self.lbl.setStyleSheet('color: red')

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())