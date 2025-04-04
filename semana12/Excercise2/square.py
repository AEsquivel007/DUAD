from shape import Shape


class Square(Shape):
    
    def __init__(self, length_side):
        self.length_side = length_side
    
    
    def calculate_area(self):
        if self.length_side <= 0:
            raise ValueError("Invalid 'length side' argument to calculate the area of the Square.")
        area = self.length_side ** 2
        return area

    
    def calculate_perimeter(self):
        if self.length_side <= 0:
            raise ValueError("Invalid 'length side' argument to calculate the perimeter of the Square.")
        perimeter = 4 * self.length_side
        return perimeter