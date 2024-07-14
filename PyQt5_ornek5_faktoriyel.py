from PyQt5.QtWidgets import QLineEdit,QPushButton,QWidget,QApplication,QVBoxLayout,QLabel
import sys

def faktoriyel():
    sayi=int(txtsayi.text())
    sayac=1
    for i in range(1,sayi+1):
        sayac=sayac*i
    sonuc.setText(str(sayac))
    
app=QApplication(sys.argv)

win=QWidget()
win.setWindowTitle("Faktöriyel Hesaplama")


lyt=QVBoxLayout()

txtsayi=QLineEdit()
lyt.addWidget(txtsayi)

sonuc=QLabel()
lyt.addWidget(sonuc)

btn=QPushButton()
btn.setText("Sonuç")
btn.clicked.connect(faktoriyel)
lyt.addWidget(btn)

win.setLayout(lyt)
win.show()
sys.exit(app.exec())

faktoriyel()
