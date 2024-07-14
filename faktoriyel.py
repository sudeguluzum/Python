sayi= int(input("Bir sayıyı giriniz: "))
if sayi<0:
    print("sayı  negatif")
elif sayi==0:
    print(sayi)
else:
    carpim=1
    for i in range(1,sayi+1):
        carpim=carpim*i
        print(carpim)



#Faktöriyel hesaplama
def faktoriyel(sayi): #faktoriyel adında bir fonskiyon tanımlıyoruz ve sayi adında bir değişken tanımlıyoruz
    toplam=1 #Çarpma işlemi yapacağımız için 1'den başlatıyoruz. 0 olsaydı sonuçta 0 çıkardı
    for i in range(1,sayi+1): #1den girilen sayı kadar döndürcek
        toplam=toplam*i
    return toplam
sayi=int(input("Bir sayı giriniz: "))
print(faktoriyel(sayi))
    
