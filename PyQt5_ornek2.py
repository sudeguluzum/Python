from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow
import sys
def window(): #Fonksiyon oluştur
    app=QApplication(sys.argv) # PyQt uygulamasını başlat
    win=QMainWindow()  #Ana penceyi oluştur
    win.setGeometry(100,100,100,100)  #Pencerenin konumu ve boyutunu ayarla
    win.setWindowTitle("Sude'nin ilk programı")  #Pencere başlığını ayarla
    
    lblInfo=QLabel(win)  #Etiket(LABEL) oluştur
    lblInfo.setGeometry(50,60,150,200) #Label'ın konumu ve boyutu
    lblInfo.setText("♥ Sude Gül Üzüm ♥") #Etiketin metni
    
    win.show() #Pencereyi göster
    sys.exit(app.exec())     # Uygulamayı başlat ve çıkış kodunu al

window() # Uygulama fonksiyonunu çağır
