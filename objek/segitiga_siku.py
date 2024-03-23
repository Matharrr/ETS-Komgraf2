from primitif.basic import segitiga_siku
from objek.bentuk_dasar import bentuk_dasar


class Segitiga_Siku(bentuk_dasar):
    def __init__(self, x, y, sisi, tinggi, tm=None):
        super().__init__(x, y, tm)
        self.sisi = sisi
        self.tinggi = tinggi

    def draw(self):
        super().draw(
            segitiga_siku(self.x, self.y, self.sisi, self.tinggi)
        )