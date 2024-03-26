from objek.ellips import Ellips
from objek.lingkaran import Lingkaran
from objek.persegi_panjang import Persegi_Panjang
from objek.segitiga_siku import Segitiga_Siku


class KatakDewasa:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.badan = Ellips(self.x, self.y, 55, 40)
        self.badan.rotate(-25)
        self.paha_kaki = Persegi_Panjang(self.x-15, self.y-20 + 20, 20, 45)
        self.paha_kaki.rotate(45)
        self.lutut = Lingkaran(self.x-38, self.y+36, 10)
        self.betis_kaki = Persegi_Panjang(self.x-3, self.y+26, 20, 45)
        self.betis_kaki.rotate(90)
        
        self.lengan_atas = Persegi_Panjang(self.x+20, self.y, 12, 33)
        self.lengan_atas.rotate(30)
        self.siku = Lingkaran(self.x+9, self.y+30, 6)
        self.lengan_bawah = Persegi_Panjang(self.x+36, self.y+24, 12, 33)
        self.lengan_bawah.rotate(90)
        
        self.mata = Lingkaran(self.x+25, self.y-25, 10)
        self.pupil = Ellips(self.x+25, self.y-25, 4, 10)

        self.mulut = Segitiga_Siku(self.x+52, self.y-8, 25, 7)
        self.mulut.mirror("y")
        
    def draw(self):
        self.badan.draw()
        self.paha_kaki.draw()
        self.lutut.draw()
        self.betis_kaki.draw()
        
        self.lengan_atas.draw()
        self.siku.draw()
        self.lengan_bawah.draw()
        
        self.mata.draw()
        self.pupil.draw()
        
        self.mulut.draw()