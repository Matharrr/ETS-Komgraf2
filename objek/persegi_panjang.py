from objek.bentuk_dasar import bentuk_dasar
from primitif.basic import persegi_panjang

class Persegi_Panjang(bentuk_dasar):
    def __init__(self, x, y, panjang, lebar, tm=None):
        super().__init__(x, y, tm)
        self.panjang = panjang
        self.lebar = lebar
        
    def draw(self):
        super().draw(
            persegi_panjang(
                self.x, self.y, self.panjang, self.lebar
            )
        )