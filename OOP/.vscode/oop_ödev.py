class Yonetici(Personel):
    def terfi(self):  1                                            
        self.maas+=523
   
    def __init__(self,isim,maas,yetenek,rutbe,yonetimBecerisi): 2
        super().__init__(isim,maas,yetenek,rutbe)
        self.yonetimBecerisi = yonetimBecerisi

    def bilgileriGoster(self): 3
        super().bilgileriGoster()
        print("Yonetim becerisi: ",self.yonetimBecerisi)
        print("*-"*20)

    def calıs(self): 4
        super().calıs()
        self.yonetimBecerisi+= 0.5
        print("Yönetim becerisi artırıldı.")