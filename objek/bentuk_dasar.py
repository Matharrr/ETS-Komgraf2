from primitif.basic import draw_bentuk
from primitif.transformasiv2 import rotate2D, transformPoints2D, translate2D, mirror2D



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
        self.tm = translate2D(dx, dy, self.tm)
        
    def rotate(self, alpha, x=None, y=None):
        if alpha is None or alpha == 0:
           alpha = 90
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        self.tm = rotate2D(alpha, x, y, self.tm)
        
    def mirror(self, axis, refx=None, refy=None):
        if refx is None:
            refx = self.x
        if refy is None:
            refy = self.y
        self.tm = mirror2D(axis, refx, refy, self.tm)
        
    def lompat_parabola(self, a, b, c, x):
        y = a*x**2 + b*x + c
        self.move(x, y)