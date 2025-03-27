class Feet:
    def __init__(self, side, toes = 5):
        self.toes = toes
        self.side = side
    
    
    def step(self):
        print(f"One step with my {self.side} feet.")
    
    
    def __str__(self):
        phrase = f"My {self.side} feet has {self.toes} toes."
        return phrase