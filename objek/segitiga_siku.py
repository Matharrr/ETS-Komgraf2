from primitif.basic import segitiga_siku
from objek.bentuk_dasar import bentuk_dasar
from primitif.line import line_dda


class Segitiga_Siku(bentuk_dasar):
    def __init__(self, x, y, sisi, tm=None):
        super().__init__(x, y, tm)
        self.sisi = sisi

    def draw(self):
        super().draw(
            segitiga_siku(self.x, self.y, self.sisi, [0,0,0,255])
        )