# Problem 1
# Mükemmel Sayı Bulma
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
toplam = 0
sayi = int(input("Lutfen bir sayi giriniz = "))
for i in range(1,sayi+1):
    if sayi % i == 0:
        toplam = toplam + i
        if toplam == sayi:
           print(str(sayi) + " Sayisi Mukemmel Sayidir.")
if toplam != sayi : 
    print("Sayi Mukemmel Degil.")
