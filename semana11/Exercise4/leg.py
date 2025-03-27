from feet import Feet


class Leg:
    def __init__(self, side):
        self.side = side
        self.feet = Feet(side)
    
    
    def walk(self):
        print(f"Moving my {self.side} leg.")
        print(self.feet)