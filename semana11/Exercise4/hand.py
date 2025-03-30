class Hand:
    def __init__(self, side, fingers = 5):
        self.fingers = fingers
        self.side = side

    
    def grab(self, item):
        print(f"My {self.side} hand is grabbing the: {item}.")
    
    
    def __str__(self):
        phrase = f"My {self.side} hand has {self.fingers} fingers."
        return phrase