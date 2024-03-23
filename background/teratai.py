from objek.ellips import Ellips

class Teratai:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.daun = Ellips(self.x, self.y, 90, 40)
        
    def draw(self):
        self.daun.draw()