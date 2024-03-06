print('''*******************************

Atm'ye Hosgeldiniz...

Lutfen yaptmak istediginiz islemi seciniz : 

1.Para Yatırma 

2.Para Çekme

3.Bakiye Sorgulama

Cıkış Yapmak Icin 'a' ya tıklayın

************************************
''')

Bakiye = 500

while True:
    islem = input("Yapmak Istediginiz Islemi Seciniz : ")
    if islem == 'a':
        print("Yine Bekleriz...")
        break
    elif islem == "1":
        toplam = float(input("Yatırmak istediginiz tutarı giriniz = "))
        Bakiye +=toplam
    elif islem == "2":
        tutar = float(input("Lutfen Cekmek isdeginiz tutarı giriniz = "))
        if tutar > Bakiye :
            print("Bakiyeniz Yetersiz Menüye Yönlendiriliyorsunuz....")
            continue
        Bakiye -=tutar  
    elif islem == "3":
        print("Bakiyeniz = " + str(Bakiye) + " TL ")
    else :
        print("Lutfen Gecerli bir islem numarası giriniz !")