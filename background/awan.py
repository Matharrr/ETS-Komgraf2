from objek.ellips import Ellips

class Awan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.awan = Ellips(self.x, self.y, 80, 40)
        self.awan1 = Ellips(self.x + 80, self.y+20, 80, 40)
        self.awan2 = Ellips(self.x - 60, self.y+60, 80, 40)
        
        
    def draw(self,):
        self.awan.draw()
        self.awan1.draw()
        self.awan2.draw()
    
    def move(self, x, y):
        self.awan.move(x, y)
        self.awan1.move(x, y)
        self.awan2.move(x, y)