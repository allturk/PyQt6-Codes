from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('window.ui', self)
        # self.show()


#         or

app = QApplication(sys.argv)
windowui = UI()
# or continue
windowui.show()

sys.exit(app.exec())
