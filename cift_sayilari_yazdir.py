#Girilen sayıya kadar çifter yazdır

sayi=int(input("Bir sayı giriniz: "))
k=1
for i in range(1,sayi+1):
    if(i%2==0):
        print(i)
