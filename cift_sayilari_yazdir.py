#Girilen sayıya kadar çifter yazdır

sayi=int(input("Bir sayı giriniz: "))
k=1
for i in range(1,sayi+1):
    if(i%2==0):
        print(i)


#0'dan başlayıp girilen sayıya kadar 2'şerli artsın
sayi=int(input("Bir sayı giriniz: "))
for i in range(0,sayi+1,2):
    print(i)



#Girilen sayıya kadar olan çift olanlarını ekrana yazdırma
def fonk(sayi):    #fonk adında bir fonksiyon tanımla ve içine sayi değişkenini at
    toplam=0     #toplamı 0'a eşitle
    for i in range(1,sayi+1):
        if i%2==0:    #sayi çift ise
            print(i)      #çift sayıları ekrana yazdır
            toplam=toplam+1     #toplamı 1 arttır
    return toplam    #toplamı döndür
sayi=int(input("Bir sayı giriniz:"))
print(fonk(sayi)) 

