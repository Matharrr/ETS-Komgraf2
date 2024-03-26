from objek.ellips import Ellips

class Telur:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.emrbio1 = Ellips(self.x, self.y, 2, 2)
        self.emrbio2 = Ellips(self.x+10, self.y, 2, 2)
        self.emrbio3 = Ellips(self.x+20, self.y, 2, 2)
        self.emrbio4 = Ellips(self.x+30, self.y, 2, 2)
        self.emrbio5 = Ellips(self.x+40, self.y, 2, 2)
        self.emrbio6 = Ellips(self.x+5, self.y+8, 2, 2)
        self.emrbio7 = Ellips(self.x+15, self.y+8, 2, 2)
        self.emrbio8 = Ellips(self.x+25, self.y+8, 2, 2)
        self.emrbio9 = Ellips(self.x+7, self.y+16, 2, 2)
        self.emrbio10 = Ellips(self.x, self.y+16, 2, 2)
        self.emrbio11 = Ellips(self.x+10, self.y+16, 2, 2)
        
        self.telur1 = Ellips(self.x, self.y, 5, 4)
        self.telur2 = Ellips(self.x+10, self.y, 5, 4)
        self.telur3 = Ellips(self.x+20, self.y, 5, 4)
        self.telur4 = Ellips(self.x+30, self.y, 5, 4)
        self.telur5 = Ellips(self.x+40, self.y, 5, 4)
        self.telur6 = Ellips(self.x+5, self.y+8, 5, 4)
        self.telur7 = Ellips(self.x+15, self.y+8, 5, 4)
        self.telur8 = Ellips(self.x+25, self.y+8, 5, 4)
        self.telur9 = Ellips(self.x+7, self.y+16, 5, 4)
        self.telur10 = Ellips(self.x, self.y+16, 5, 4)
        self.telur11 = Ellips(self.x+10, self.y+16, 5, 4)
        
    def draw(self):
        self.emrbio1.draw()
        self.emrbio2.draw()
        self.emrbio3.draw()
        self.emrbio4.draw()
        self.emrbio5.draw()
        self.emrbio6.draw()
        self.emrbio7.draw()
        self.emrbio8.draw()
        self.emrbio9.draw()
        self.emrbio10.draw()
        self.emrbio11.draw()
        
        self.telur1.draw()
        self.telur2.draw()
        self.telur3.draw()
        self.telur4.draw()
        self.telur5.draw()
        self.telur6.draw()
        self.telur7.draw()
        self.telur8.draw()
        self.telur9.draw()
        self.telur10.draw()
        self.telur11.draw()