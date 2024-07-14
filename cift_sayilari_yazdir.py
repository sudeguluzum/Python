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
