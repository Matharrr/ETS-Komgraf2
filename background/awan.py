from objek.ellips import Ellips

class Awan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.awan = Ellips(self.x, self.y, 80, 40)
        self.awan1 = Ellips(self.x + 40, self.y - 20, 80, 40)
        self.awan2 = Ellips(self.x - 40, self.y - 20, 80, 40)
        self.awan3 = Ellips(self.x + 20, self.y - 40, 80, 40)
        self.awan4 = Ellips(self.x - 20, self.y - 40, 80, 40)
        
        
    def draw(self):
        self.awan.draw()
        self.awan1.draw()
        self.awan2.draw()
        self.awan3.draw()
        self.awan4.draw()