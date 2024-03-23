import math

class CartesianConverter:
    def __init__(self, width, height, margin):
        self.width = width
        self.height = height
        self.margin = margin

    def convert_to_cartesian(self, xa, ya):
        axis = math.ceil(self.width/2)
        ordinat = math.ceil(self.height/2)
        
        return [axis+xa, ordinat-ya]