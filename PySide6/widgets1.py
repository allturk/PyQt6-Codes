from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Widgets")
        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(20)
        widget.setFont(font)
        # widget.setFont(QFont("Ethnocentric",20,QFont.Weight.Bold,False))
        widget.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.setCentralWidget(widget)


app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec())
