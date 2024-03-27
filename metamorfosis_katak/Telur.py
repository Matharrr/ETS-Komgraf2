from objek.ellips import Ellips

class Telur:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.emrbio1 = Ellips(self.x, self.y, 2, 2)
        
        self.telur1 = Ellips(self.x, self.y, 5, 4)
        
    def draw(self):
        self.emrbio1.draw()
        
        self.telur1.draw()
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.emrbio1.move(-dx, dy)
        self.telur1.move(-dx, dy)