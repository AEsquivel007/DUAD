from hand import Hand


class Arm:
    def __init__(self, side):
        self.hand = Hand(side)
        self.side = side
    
    
    def mover(self):
        print(f"Estoy moviendo el brazo {self.side}.")
        print(self.hand)