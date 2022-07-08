from PySide6.QtWidgets import(
    QApplication,
    QMainWindow,
    QPushButton,
)

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyside6 Signal App')
        button = QPushButton('Click Me')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print('Button Clicked')

    def the_button_was_toggled(self,checked):
        print('Checked?',checked)

app= QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())