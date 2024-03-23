from objek.ellips import Ellips
from objek.segitiga_siku import Segitiga_Siku


class KatakDewasa:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.badan = Ellips(self.x, self.y, 50, 40)
        self.badan.rotate(-25)
        
    def draw(self):
        self.badan.draw()