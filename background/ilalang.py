from objek.persegi_panjang import Persegi_Panjang
from objek.bentuk_dasar import bentuk_dasar

class Ilalang(bentuk_dasar):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tangkai = Persegi_Panjang(self.x, self.y-50, 4, 200)
        self.tangkai2 = Persegi_Panjang(self.x, self.y, 60, 4)
        self.tangkai2.rotate(-45)
        self.tangkai3 = Persegi_Panjang(self.x, self.y+30, 80, 4)
        self.tangkai3.rotate(-45)
        self.tangkai4 = Persegi_Panjang(self.x, self.y+60, 80, 4)
        self.tangkai4.rotate(-45)
        
    def draw(self):
        self.tangkai.draw()
        self.tangkai2.draw()
        self.tangkai3.draw()
        self.tangkai4.draw()