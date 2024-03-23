from objek.bentuk_dasar import bentuk_dasar
from primitif.basic import ellips

class Ellips(bentuk_dasar):
    def __init__(self, x, y, rx, ry, tm=None):
        super().__init__(x, y, tm)
        self.rx = rx
        self.ry = ry

    def draw(self):
        super().draw(
            ellips(
                self.x, self.y, self.rx, self.ry
            )
        )