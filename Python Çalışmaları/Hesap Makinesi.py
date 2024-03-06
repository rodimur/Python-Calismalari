print(''' Hesap Makinesi 
''')
print("Lutfen 2 sayi giriniz")
x = int(input("Sayi1 = "))
y = int(input("Sayi2 = "))
print(''' ***Lutfen Yapmak Istediginiz Islemi Seciniz *** 
-Toplama Islemi = 1
-Cıkartma Islemi = 2
-Bolme Islemi = 3
-Carpma Islemi = 4
''')
islem = int(input())
if islem == 1:
    sonuc = x + y
    print("Toplama isleminizin Sonucu = " + str(sonuc))
elif islem == 2:
    sonuc = x - y
    print("Cıkartma isleminizin Sonucu = " + str(sonuc))
elif islem == 3:
    sonuc = x / y
    print("Bolme isleminizin Sonucu = " + str(sonuc))
elif islem == 4:
    sonuc = x * y
    print("Carpma isleminizin Sonucu = " + str(sonuc))
else :
    print("Lutfen Gecerli Bir Islem Giriniz !")
