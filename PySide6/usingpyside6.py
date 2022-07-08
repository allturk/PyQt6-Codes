from PySide6.QtWidgets import QApplication,QWidget,QPushButton
import sys

# app=QApplication([])
app=QApplication(sys.argv)
window=QWidget()
# window=QPushButton('Click Me')

window.show()

sys.exit(app.exec())
