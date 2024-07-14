#1'den sayi'ye kadar olan sayıların toplamını hesaplar ve her adımda bu toplamı ekrana yazdırır
sayi=6
toplam =0
for i in range(1,sayi+1):
    toplam+=i   # toplam değişkenine i eklenir
    print(toplam)  # her adımda toplam değeri ekrana yazdırılır


#1'den kullanıcının girdiği sayıya kadar olan sayıları toplayan ve toplamı döndüren bir fonksiyon
def topla(sayi):
    toplam=0
    for i in range(1,sayi+1):
        toplam+=i
    return toplam  # toplam değerini fonksiyon çağrıldığı yere döndür

sayi=int(input("Bir sayı giriniz:"))
print(topla(sayi))

# =============================================================================

def topla(sayi):
    toplam=0
    for i in range(1,sayi+1):
        toplam+=i
    return toplam

def topla2(sayi):
    return(sayi*(sayi+1))/2

sayi=int(input("Bir sayı giriniz: "))
print(topla(sayi))
print(topla2(sayi))
