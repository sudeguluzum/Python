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
    
