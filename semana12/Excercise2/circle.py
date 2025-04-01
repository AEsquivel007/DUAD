from shape import Shape
import math


class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__()
        self.pi = math.pi
        self.radius = radius
    
    
    def calculate_area(self):
        if self.radius <= 0:
            print("Invalid radius to calculate the area of the circle!!!")
        area = self.pi * self.radius ** 2
        return area
    
    
    def calculate_perimeter(self):
        if self.radius <= 0:
            print("Invalid radius to calculate the perimeter of the circle!!!")
        perimeter = 2 * self.pi * self.radius
        return perimeter