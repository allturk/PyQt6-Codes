from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('PyQt6 Study')
        self.setWindowIcon(QIcon('../images/computer.png'))
        self.create_checkbox()


    def create_checkbox(self):
        self.hbox = QHBoxLayout()
        self.cb1 = QCheckBox('Python', self)
        self.cb1.move(20, 20)
        self.cb1.setIcon(QIcon('../images/python.png'))
        self.cb1.setIconSize(QSize(20, 20))
        self.cb1.setFont(QFont("Sanserif", 13))

        self.cb2 = QCheckBox('Java', self)
        self.cb2.move(20, 20)
        self.cb2.setIcon(QIcon('../images/java.png'))
        self.cb2.setIconSize(QSize(20, 20))
        self.cb2.setFont(QFont("Sanserif", 13))

        self.cb3 = QCheckBox('JavaScript', self)
        self.cb3.move(20, 20)
        self.cb3.setIcon(QIcon('../images/javascript.png'))
        self.cb3.setIconSize(QSize(20, 20))
        self.cb3.setFont(QFont("Sanserif", 13))

        self.label = QLabel("Hello")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label.setFont(QFont("Sanserif", 15))

        vbox = QVBoxLayout()
        vbox.addStretch()
        self.hbox.addWidget(self.cb1)
        self.hbox.addWidget(self.cb2)
        self.hbox.addWidget(self.cb3)
        self.cb3.toggled.connect(self.item_selected)
        self.cb2.toggled.connect(self.item_selected)
        self.cb1.toggled.connect(self.item_selected)
        vbox.addLayout(self.hbox)
        vbox.addStretch()
        vbox.addWidget(self.label)
        vbox.addStretch()

        self.setLayout(vbox)

    def item_selected(self):
        value = ""
        for i in range(self.hbox.count()):
            cbox=self.hbox.itemAt(i).widget()
            if cbox.isChecked():
                value =  f"{cbox.text()} {value}"
        self.label.setText(f"You have selected {value}")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
