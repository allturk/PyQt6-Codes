from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First PySide6 App')
        button = QPushButton('Click Me')

        # self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(200, 150))
        self.setMaximumSize(QSize(400, 300))
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
