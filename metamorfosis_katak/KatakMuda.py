from objek.ellips import Ellips
from objek.segitiga_kaki import Segitiga_Kaki
from objek.segitiga_siku import Segitiga_Siku


class KatakMuda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.badan = Ellips(self.x, self.y, 27, 38)
        self.ekor = Segitiga_Kaki(self.x-37, self.y-10, 20, 30)
        self.mata1 = Ellips(self.x+20, self.y-10, 2, 2)
        self.mata_luar1 = Ellips(self.x+20, self.y-10, 6, 5)
        self.mata2 = Ellips(self.x+20, self.y+10, 2, 2)
        self.mata_luar2 = Ellips(self.x+20, self.y+10, 6, 5)
        self.badan.rotate(90)
        self.ekor.rotate(90)
        self.paha_kaki1 = Segitiga_Siku(self.x-10, self.y+24, 15, 22)
        self.paha_kaki1.mirror("y")
        self.kaki1 = Segitiga_Siku(self.x-35, self.y+41, 14, 26)
        self.kaki1.rotate(280)
        self.paha_kaki2 = Segitiga_Siku(self.x-10, self.y-24, 15, 22)
        self.paha_kaki2.rotate(180)
        self.kaki2 = Segitiga_Siku(self.x-35, self.y-41, 14, 26)
        self.kaki2.mirror("x")
        self.kaki2.rotate(80)
        
        self.jari_kiri_kaki1 = Segitiga_Kaki(self.x-35, self.y-37, 8, 10)
        self.jari_kiri_kaki1.rotate(130)
        self.jari_kiri_kaki2 = Segitiga_Kaki(self.x-35, self.y-35, 9, 15)
        self.jari_kiri_kaki2.rotate(90)
        self.jari_kiri_kaki3 = Segitiga_Kaki(self.x-35, self.y-31, 8, 10)
        self.jari_kiri_kaki3.rotate(50)
        
        self.jari_kanan_kaki1 = Segitiga_Kaki(self.x-35, self.y+31, 8, 10)
        self.jari_kanan_kaki1.rotate(50)
        self.jari_kanan_kaki2 = Segitiga_Kaki(self.x-35, self.y+29, 9, 15)
        self.jari_kanan_kaki2.rotate(90)
        self.jari_kanan_kaki3 = Segitiga_Kaki(self.x-35, self.y+25, 8, 10)
        self.jari_kanan_kaki3.rotate(130)
        
        self.lengan_atas_kiri = Segitiga_Siku(self.x, self.y-27, 10, 20)
        self.lengan_atas_kiri.mirror("y")
        self.lengan_atas_kiri.rotate(180)
        self.lengan_atas_kanan = Segitiga_Siku(self.x, self.y+27, 10, 20)
        
        self.lengan_bawah_kiri = Segitiga_Siku(self.x+20, self.y-47, 10, 20)
        self.lengan_bawah_kiri.rotate(90)
        self.lengan_bawah_kanan = Segitiga_Siku(self.x+20, self.y+47, 10, 20)
        self.lengan_bawah_kanan.mirror("y")
        self.lengan_bawah_kanan.rotate(90)
        
        
    def draw(self):
        self.badan.draw()
        self.ekor.draw()
        self.mata1.draw()
        self.mata_luar1.draw()
        self.mata2.draw()
        self.mata_luar2.draw()
        self.paha_kaki1.draw()
        self.kaki1.draw()
        self.paha_kaki2.draw()
        self.kaki2.draw()
        self.jari_kiri_kaki1.draw()
        self.jari_kiri_kaki2.draw()
        self.jari_kiri_kaki3.draw()
        self.jari_kanan_kaki1.draw()
        self.jari_kanan_kaki2.draw()
        self.jari_kanan_kaki3.draw()
        self.lengan_atas_kiri.draw()
        self.lengan_atas_kanan.draw()
        self.lengan_bawah_kiri.draw()
        self.lengan_bawah_kanan.draw()