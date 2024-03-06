# Problem 1
# beden kitle indeksini hesaplama
boy = float(input("Lutfen Boyunuzu giriniz = "))
kilo = float(input("Lutfen Kilonuzu giriniz = "))
bki = kilo  / (boy * boy)

if bki  < 18.5 :
    print("Zayıfsınız")
elif bki > 18.5 and bki < 25 :
    print("Normalsiniz")
elif bki > 25 and bki < 30 :
    print("Fazla kilolusunuz")
elif bki > 30 :
    print("Obez")
else :
    print("Lutfen degerleri Kontrol ediniz !")



# Problem 2
# 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın
print("Lutfen 3 tane sayi giriniz ")
sayi1 = float(input("1.Sayi = "))
sayi2 = float(input("2.Sayi = "))
sayi3 = float(input("3.Sayi = "))

if sayi1 == sayi2 == sayi3:
    print(sayi1)
elif sayi1 == sayi2 < sayi3:
    print(sayi1)
elif sayi1 < sayi2 == sayi3:
    print(sayi2)
elif sayi1 == sayi3 < sayi2:
    print(sayi2)
elif sayi1 < sayi2 < sayi3:
    print(sayi3)
elif sayi1 < sayi3 < sayi2:
    print(sayi2)
elif sayi3 < sayi1 < sayi2:
    print(sayi2)
elif sayi3 < sayi2 < sayi1:
    print(sayi1)
elif sayi2 < sayi1 < sayi3:
    print(sayi3)
elif sayi2 < sayi3 < sayi1:
    print(sayi1)


# Problem 3
# vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın
print('''
    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.
''')
Vize1 = float(input("Lutfen 1.vize Notunuzu Giriniz = "))
Vize2 = float(input("Lutfen 2.vize Notunuzu Giriniz = "))
Final = float(input("Lutfen Final Notunuzu Giriniz = "))

sonuc = (Vize1 * 0.3) + (Vize2 * 0.3 ) + (Final * 0.4)
if sonuc >= 90:
    print("AA")
elif sonuc >= 95:
    print("BA")
elif sonuc >= 80:
    print("BB")
elif sonuc >= 75:
    print("CB")
elif sonuc >= 70:
    print("CC")
elif sonuc >= 65:
    print("DC")
elif sonuc >= 60:
    print("DD")
elif sonuc >= 55:
    print("FD")
elif sonuc >= 50:
    print("FF Ile Kaldınız Lutfen Bute Giriniz ")
    BütNotu = float(input("Büt notunuzu Giriniz = "))
    sonuc2 = (Vize1 * 0.3) + (Vize2 * 0.3 ) + (BütNotu * 0.4)
    if sonuc >= 90:
        print("AA")
    elif sonuc2 >= 95:
         print("BA")
    elif sonuc2 >= 80:
         print("BB")
    elif sonuc2 >= 75:
         print("CB")
    elif sonuc2 >= 70:
         print("CC")
    elif sonuc2 >= 65:
         print("DC")
    elif sonuc2 >= 60:
         print("DD")
    elif sonuc >= 55:
         print("FD")
    elif sonuc >= 50:
         print("FF")














