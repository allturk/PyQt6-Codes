from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(410, 290, 700, 400)
        self.setWindowTitle('Python Labels')
        self.setWindowIcon(QIcon('../images/computer.png'))
        # label=QLabel("Python Gui Development",self)
        # # label.setText("New text here")
        # label.move(100,100)
        # label.setFont(QFont("Sansserif",20))
        # label.setStyleSheet("color: navy")
        # # self.show()
        # label.setText(str(12))
        # label.setNum(15)
        # label.clear()

        # label=QLabel(self)
        # pixmap=QPixmap('../images/computer.png')
        # label.setPixmap(pixmap)

        label = QLabel(self)
        movie = QMovie("../images/sky.gif")
        movie.setSpeed(100)
        movie.setScaledSize(QSize(200, 200))
        label.setMovie(movie)
        movie.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
