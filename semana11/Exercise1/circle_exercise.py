import math


class Circle:
    
    def __init__(self, radius):
        self.pi = math.pi
        self.radius = radius
    
    
    def get_area(self):
        area = self.pi * (self.radius**2)
        return area

my_circle = Circle(5)

print(f"El área calculada es de: {my_circle.get_area()}")