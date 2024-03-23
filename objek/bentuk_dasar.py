from primitif.basic import draw_bentuk
from primitif.transformasiv2 import rotate2D, transformPoints2D, translate2D



class bentuk_dasar:
    def __init__(self, x, y, tm=None):
        self.x = x
        self.y = y
        self.tm = tm
    
    def draw(self, bidang):
        draw_bentuk(
            transformPoints2D(bidang, self.tm)
        )
        
    def move(self, dx, dy):
        self.tm = translate2D(dx, dy)
        
    def rotate(self, alpha, x=None, y=None):
        if alpha is None or alpha == 0:
           alpha = 90
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.tm = rotate2D(alpha, x, y, self.tm)