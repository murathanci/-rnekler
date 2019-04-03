
class Personel():
    mesai = "9 -18"
    sirket = "AS-AS"

    def __init__(self,isim,maas,yetenek,rutbe):  1
        self.isim = isim
        self.yetenek = yetenek
        self.maas = maas
        self.gunsayisi = 0
        self.rutbe = rutbe,

    def calıs(self):                             2
        print(self.isim,"çalışıyor")
        self.gunsayisi+=1

    def terfi(self):                             3
        print("Tebrikler ",self.isim,"Terfi aldın")
        self.maas+=200

    def bilgileriGoster(self):                   4
        print("*-"*20)
        print("Personelin ismi: ",self.isim)
        print("Personelin yetenekleri: ",self.yetenek)
        print("Personelin maaşı: ",self.maas)
        print("Personelin toplam gün sayısı",self.gunsayisi)
        print("Personelin konumu: ",self.rutbe)
        print("*-"*20)