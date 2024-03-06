class Çalışan ():
    def __init__(self,adi,soyadi,maasi,departman):
        print("init fonksiyonu cagırıldı")
        self.adi = adi
        self.soyadi = soyadi
        self.maasi = maasi
        self.departman = departman
    def bilgilerigöster(self):
        print("Çalışan Sınıfının Bilgileri.....")
        print("İsim = {} \nSoyisim = {} \nMaaşı = {} \nDepartman = {} ".format(self.adi,self.soyadi,self.maasi,self.departman))

    def departman_degistir(self,yeni_departman):
        print("Departman Değiştiriliyor....")
        self.departman = yeni_departman

class Yönetici(Çalışan):
    def zam_yap(self,zam):
        print("Zam Yapılıyor.....")
        self.maasi += zam

yönetici = Yönetici("Tunahan","Balci",0,"Öğrenci")
yönetici.bilgilerigöster()

yönetici.departman_degistir("Öğrenci Değil")
yönetici.bilgilerigöster()


yönetici.zam_yap(500)
yönetici.bilgilerigöster()
