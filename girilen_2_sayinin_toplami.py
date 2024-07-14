sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))

toplam=0
for i in range(1,sayi2+1):  # 1'den sayi2'ye kadar olan sayi1'i topla
    toplam=toplam+sayi1
print(toplam)
