class Çalışan ():
    def __init__(self,adi,soyadi,maasi,departman):
        print("Çalışan sınıfının init fonksiyonu cagırıldı")
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
    def __init__(self,adi,soyadi,maasi,departman,kişi_sayısı):
        super().__init__(adi,soyadi,maasi,departman)
        
        print("Yönetici Sınıfının init fonksiyonu cagırıldı")
        
        self.kişi_sayısı = kişi_sayısı
    
    
    def bilgilerigöster(self):
        print("Çalışan Sınıfının Bilgileri.....")
        print("İsim = {} \nSoyisim = {} \nMaaşı = {} \nDepartman = {} \nSorumu Kişi Sayısı = {} ".format(self.adi,self.soyadi,self.maasi,self.departman,self.kişi_sayısı))
    
    
    def zam_yap(self,zam):
        print("Zam Yapılıyor.....")
        self.maasi += zam

#şimdi burda olay şu yönetici çalışandan miras alıyo overriding yapıyo ancak ad soyad maaş ve departmanı tekrardan yazmamak için onu super() anahtar kelimesi ile çalışandan çekiyor 