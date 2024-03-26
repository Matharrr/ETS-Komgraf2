from objek.bentuk_dasar import bentuk_dasar
from primitif.basic import lingkaran

class Lingkaran(bentuk_dasar):
    def __init__(self, x, y, r, tm=None):
        super().__init__(x, y, tm)
        self.r = r
        
    def draw(self):
        super().draw(
            lingkaran(
                self.x, self.y, self.r
            )
        )