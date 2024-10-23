class Kitap:
    def __init__(self,baslik,yazar,mevcut=True):
        self.baslik=baslik
        self.yazar=yazar
        self.mevcut=mevcut
    def oduncAl(self):
        if self.mevcut:
            self.mevcut=False
            return f"kitap '{self.baslik}' ödünç alındı"
        else:
            return f"kitap '{self.baslik}' zaten ödünç alındı"
    def iadeEt(self):
        self.mevcut=True
        return f"kitap '{self.baslik}' geri iade edildi"

class Kutuphane:
    def __init__(self):
        self.kitaplar=[]
    def kitapEkle(self,kitap):
        self.kitaplar.append(kitap)
    def kitaplariListele(self):
        for kitap in self.kitaplar:
            durum="Mevcut" if kitap.mevcut else "ödünçte"
            print(f"{kitap.baslik}-{kitap.yazar}({durum})")
    def kitapBul(self,baslik):
        for kitap in self.kitaplar:
            if kitap.baslik==baslik:
                return kitap
        return None

kutuphane=Kutuphane()
kitap1=Kitap("1984","George Orwell")
kitap2=Kitap("Savaş ve Barış","Lev Tolstoy")
kutuphane.kitapEkle(kitap1)
kutuphane.kitapEkle(kitap2)
kutuphane.kitaplariListele()
print(kitap1.oduncAl())
kutuphane.kitaplariListele()
print(kitap1.iadeEt())
kutuphane.kitaplariListele()
