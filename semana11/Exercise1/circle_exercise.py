class Circle:
    pi = 3.1416
    radius = 5
    
    def get_area(self):
        area = self.pi * (self.radius**2)
        return area

my_circle = Circle()
print(f"El área calculada es de: {my_circle.get_area()}")