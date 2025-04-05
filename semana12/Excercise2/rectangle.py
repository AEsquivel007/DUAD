from shape import Shape


class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    
    def calculate_area(self):
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Invalid 'width or length' arguments to calculate the area of the Rectangle.")
        area = self.length * self.width
        return area
    
    
    def calculate_perimeter(self):
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Invalid 'width or length' arguments to calculate the perimeter of the Rectangle.")
        perimeter = 2 * (self.length + self.width)
        return perimeter