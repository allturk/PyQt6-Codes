from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyside6 Signal App')
        self.button = QPushButton('Click Me')
        self.button_is_checked=True
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked=self.button.isChecked()
        print(self.button_is_checked)

app= QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())

