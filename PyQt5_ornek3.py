from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QTextEdit
from PyQt5.QtGui import QFont
import sys


def sude():
    app=QApplication(sys.argv)
    
    win=QMainWindow()
    win.setWindowTitle("Kayıt")
    win.setGeometry(600,250,500,500)
    
    lblBaslik=QLabel(win)
    lblBaslik.setText("Stok Kartı")
    lblBaslik.setFont(QFont("Arial",25,2,True))
    lblBaslik.setGeometry(200,0,500,50)
    lblBaslik.setStyleSheet("color:purple")

    lblStok=QLabel(win)
    lblStok.setText("Stok Kodu")
    lblStok.setGeometry(30,50,500,50)
    
    lblKutu=QTextEdit(win)
    lblKutu.setGeometry(150,50,250,50)

    win.show()
    sys.exit(app.exec())
sude()
