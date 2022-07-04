from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage('Welcome to PyQt6')
window.menuBar().addMenu('File')
window.show()

sys.exit(app.exec())   # This is the same as app.exec_()
