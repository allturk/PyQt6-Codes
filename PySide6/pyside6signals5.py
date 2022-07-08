from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
import sys
from random import choice
window_titles = [
"My App",
"My App",
"Still My App",
"Still My App",
"What on earth",
"What on earth",
"This is surprising",
"This is surprising",
"Something went wrong",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked=0
        self.setWindowTitle("PySide6 Signal App")

        self.button = QPushButton('Click Me')
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)
    def the_button_was_clicked(self):
        self.n_times_clicked += 1
        print("Button Clicked")
        new_window_title = choice(window_titles)
        print("Setting title: %s"%new_window_title)
        self.setWindowTitle(new_window_title)


    def the_window_title_changed(self,new_title):
        print("Window title changed to: %s"%new_title)
        if new_title=="Something went wrong":
            self.button.setDisabled(True)
            print(f"{self.n_times_clicked} times clicked")


app= QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())