from objek.ellips import Ellips
from objek.segitiga_kaki import Segitiga_Kaki


class Kecebong:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.badan = Ellips(self.x, self.y, 18, 40)
        self.ekor = Segitiga_Kaki(self.x-39, self.y-8, 15, 82)
        self.mata1 = Ellips(self.x+20, self.y-10, 2, 2)
        self.mata_luar1 = Ellips(self.x+20, self.y-10, 6, 5)
        self.mata2 = Ellips(self.x+20, self.y+10, 2, 2)
        self.mata_luar2 = Ellips(self.x+20, self.y+10, 6, 5)
        self.badan.rotate(90)
        self.ekor.rotate(90)
        
    def rotate_all(self, angle):
        self.badan.rotate(angle)
        self.ekor.rotate(angle)
        self.mata1.rotate(angle)
        self.mata_luar1.rotate(angle)
        self.mata2.rotate(angle)
        self.mata_luar2.rotate(angle)
        
    def draw(self):
        self.badan.draw()
        self.ekor.draw()
        self.mata1.draw()
        self.mata_luar1.draw()
        self.mata2.draw()
        self.mata_luar2.draw()
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.badan.move(dx*0.28, dy*-4.55)
        self.ekor.move(dx*0.28, dy*-4.55)
        self.mata1.move(dx*1.14, dy*1.14)
        self.mata_luar1.move(dx*1.14, dy*1.14)
        self.mata2.move(dx*1.14, dy*1.14)
        self.mata_luar2.move(dx*1.14, dy*1.14)