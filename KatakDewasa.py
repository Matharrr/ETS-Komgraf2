from objek.ellips import Ellips
from objek.segitiga_siku import Segitiga_Siku
from objek.persegi_panjang import Persegi_Panjang


class KatakDewasa:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.badan = Ellips(self.x, self.y, 50, 40)
        self.badan.rotate(-25)
        self.paha_kaki = Persegi_Panjang(self.x-20, self.y + 20, 20, 40)
        
    def draw(self):
        self.badan.draw()
        self.paha_kaki.draw()