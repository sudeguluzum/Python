#Girilen 2 sayının çarpını veren program
def carpma(sayi1,sayi2):
    toplam=0
    for i in range(1,sayi2+1):
        toplam=toplam+sayi1
    return toplam

sayi1=int(input("Birinici Sayıyı Giriniz: "))
sayi2=int(input("İkinci Sayıyı Giriniz: "))
print(carpma(sayi1,sayi2))

