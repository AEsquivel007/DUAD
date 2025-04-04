from shape import Shape
import math


class Circle(Shape):
    
    def __init__(self, radius):
        self.pi = math.pi
        self.radius = radius
    
    
    def calculate_area(self):
        if self.radius <= 0:
            raise ValueError("Invalid 'radius' argument to calculate the area of the Circle.")
        area = self.pi * self.radius ** 2
        return area
    
    
    def calculate_perimeter(self):
        if self.radius <= 0:
            raise ValueError("Invalid 'radius' argument to calculate the perimeter of the Circle.")
        perimeter = 2 * self.pi * self.radius
        return perimeter