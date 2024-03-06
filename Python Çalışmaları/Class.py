#şimdi bu alttaki gibi class oluşturursan eğer tek bir veri oluyo yani bu değişmiyo özellikler hep aynı 
"""
class araba ():
    Model = "Skoda"
    Renk = "Mavi"
    Beygir_gucu = 100
    Silindir = 10

araba1 = araba()
araba2 = araba()
print(araba1)
print(araba1.Beygir_gucu)
"""



#__init__ sayesinde farklı farklı yapabiliyoruz
"""
class araba ():
    def __init__(self,Model,Renk,Beygir_gucu,Silindir):
        print("init fonksiyonu cagırıldı")
        self.Model = Model
        self.Renk = Renk
        self.Beygir_gucu = Beygir_gucu
        self.Silindir = Silindir

araba1 = araba("Reno","Mavi",100,4)
araba2 = araba("skoda","siyah",110,4)

print(araba1.Model)
print(araba1.Renk)
print(araba1.Beygir_gucu)
print(araba1.Silindir)
print(araba2.Model)
print(araba2.Renk)
print(araba2.Beygir_gucu)
print(araba2.Silindir)
"""




class Yazılımcı ():
    def __init__(self,adi,soyadi,numarasi,maasi,diller):
        print("init fonksiyonu cagırıldı")
        self.adi = adi
        self.soyadi = soyadi
        self.numarasi = numarasi
        self.maasi = maasi
        self.diller = diller

    def bilgiler(self):
        print("""

        Bilgiler
        
        Adı = {}

        Soyadi = {}

        Numarasi = {}

        Maasi = {}

        Bildigi Diller = {}


        """.format(self.adi,self.soyadi,self.numarasi,self.maasi,self.diller))
    
    def zam_yap(self,zam_miktari):
        print("Zam Yapiliyor....")
        self.maasi += zam_miktari

    def dil(self,dil_ekle):
        print("Yeni Dil Ekleniyor....")
        self.diller.append(dil_ekle)

yazılımcı = Yazılımcı("Tunahan","Balci",345456,0,["Python","C++"])
print(yazılımcı)
yazılımcı.bilgiler()
yazılımcı.zam_yap(1)
yazılımcı.dil("Js")
yazılımcı.bilgiler()

















