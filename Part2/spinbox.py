from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("../images/computer.png"))
        self.setWindowTitle("PyQt6 SpinBox")
        hbox = QHBoxLayout()
        self.label = QLabel("Laptop Price: ")
        self.label.setFont(QFont("Times", 15))
        self.linedit=QLineEdit()
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)
        self.total_result=QLineEdit()
        hbox.addWidget(self.label)
        hbox.addWidget(self.linedit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.total_result)

        self.setLayout(hbox)
    def spin_selected(self):
        if self.linedit.text()!=0:
            price=int(self.linedit.text())
            totalPrice=self.spinbox.value()*price
            self.total_result.setText(str(totalPrice))
        else:
            print("Wrong value!")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
