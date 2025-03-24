from feet import Feet


class Leg:
    def __init__(self, side):
        self.side = side
        self.feet = Feet(side)
    
    
    def caminar(self):
        print(f"Moviendo la pierna {self.side}.")
        print(self.feet)