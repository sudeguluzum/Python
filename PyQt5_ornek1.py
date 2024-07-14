from PyQt5.QtWidgets import QApplication,QLabel
import sys
app=QApplication([])
lblInfo=QLabel("Hello World")
lblInfo.show()
sys.exit(app.exec())
