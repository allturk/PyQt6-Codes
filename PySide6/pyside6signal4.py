from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyside6 Signal App')
        self.button = QPushButton('Click Me')
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me!")
        self.button.setEnabled(False)

        self.setWindowTitle("My Oneshot App")

app= QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec())

