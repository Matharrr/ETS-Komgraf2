from primitif import basic

class Body:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        ellipe = basic.Ellipse(self.x, self.y, 100, 100)
        print (ellipe)
        
class Eyes:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Tail:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class RightLeg:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class LeftLeg:
    def __init__(self, x, y):
        self.x = x
        self.y = y