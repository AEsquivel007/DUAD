from shape import Shape


class Rectangle(Shape):
    
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    
    def calculate_area(self):
        if self.length <= 0 or self.width <= 0:
            print("Invalid length or width to calculate the area of the rectangle!!!")
        area = self.length * self.width
        return area
    
    
    def calculate_perimeter(self):
        if self.length <= 0 or self.width <= 0:
            print("Invalid length or width to calculate the perimeter of the rectangle!!!")
        perimeter = 2 * (self.length + self.width)
        return perimeter