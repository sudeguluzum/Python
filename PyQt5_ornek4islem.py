  from PyQt5.QtWidgets import QApplication,QHBoxLayout,QLabel,QWidget,QLineEdit,QPushButton
import sys
def topla():
    sayi1=int(txtsayi1.text())
    sayi2=int(txtsayi2.text())
    cikti.setText(str(sayi1+sayi2))
def carp():    
    sayi1=int(txtsayi1.text())
    sayi2=int(txtsayi2.text())
    cikti.setText(str(sayi1*sayi2))
    
def cikar():
    sayi1=int(txtsayi1.text())
    sayi2=int(txtsayi2.text())
    cikti.setText(str(sayi1-sayi2))
    
def bolme():
    sayi1=int(txtsayi1.text())
    sayi2=int(txtsayi2.text())
    cikti.setText(str(sayi1/sayi2))
app=QApplication(sys.argv)
    
win=QWidget()
win.setWindowTitle("4 işlem programı")
    
    
lyt=QHBoxLayout()
    
txtsayi1=QLineEdit()
lyt.addWidget(txtsayi1)
    
txtsayi2=QLineEdit()
lyt.addWidget(txtsayi2)
    
cikti=QLineEdit()
cikti.setEnabled(False)
lyt.addWidget(cikti)
    
btn=QPushButton()
btn.setText("Topla")
btn.clicked.connect(topla)
lyt.addWidget(btn)

btn2=QPushButton()
btn2.setText("Çarp")
btn2.clicked.connect(carp)
lyt.addWidget(btn2)

btn3=QPushButton()
btn3.setText("Çıkar")
btn3.clicked.connect(cikar)
lyt.addWidget(btn3)

btn4=QPushButton()
btn4.setText("Bölme")
btn4.clicked.connect(bolme)
lyt.addWidget(btn4)


win.setLayout(lyt)
win.show()
sys.exit(app.exec())

topla()
