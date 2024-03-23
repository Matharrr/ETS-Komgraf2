from objek.ellips import Ellips
from objek.segitiga_siku import Segitiga_Siku


class Kecebong_Berkaki:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.badan = Ellips(self.x, self.y, 20, 30)
        self.ekor = Segitiga_Siku(self.x, self.y, 20, 30)
        self.badan.rotate(90)
        self.ekor.rotate(-90)
        self.mata = Ellips(self.x+10, self.y-10, 5, 5)
        
    def draw(self):
        self.badan.draw()
        self.ekor.draw()
        self.mata.draw()