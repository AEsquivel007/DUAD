from hand import Hand


class Arm:
    def __init__(self, side):
        self.hand = Hand(side)
        self.side = side
    
    
    def move(self):
        print(f"I'm moving my {self.side} arm.")
        print(self.hand)