#Girilen sayının Mükemmel Sayı olup olmadığını sorgulayan
sayi=int(input("Bir sayı giriniz: "))   
toplam=0
for i in range(1,sayi):
    if(sayi%i==0):
        toplam=toplam+i
if(sayi==toplam):
    print("Mükemmel Sayı")
else:
    print("Mükemmel sayı değil")



#Girilen sayının mükemmel sayı olup olmadığını yazan fonksiyon
def ms(sayi):
    toplam=0
    for i in range(1,sayi):
        if(sayi%i==0):
            toplam=toplam+i
    if(sayi==toplam):
        print("Mükemmel Sayı")
    else:
        print("Mükemmel Sayı Değildir")
sayi=int(input("Bir sayı giriniz:"))
ms(sayi)




#Girilen sayıya kadar olan mükemmel sayıları gösterek program
def ms(sayi):
    toplam=0
    for i in range(1,sayi):
        if(sayi%i==0):   # Eğer sayi, i'ye tam bölünüyorsa
            toplam=toplam+i  # i'yi toplam değişkenine ekle
    if(sayi==toplam):  # Eğer sayi, bölenlerinin toplamına eşitse, bu bir mükemmel sayıdır
        print("Mükemmel Sayı",sayi)

sayi=int(input("Bir sayı giriniz: "))

for k in range(1,sayi+1): # 1'den sayi'ye kadar olan her sayı için ms fonksiyonunu çağır
    ms(k)
