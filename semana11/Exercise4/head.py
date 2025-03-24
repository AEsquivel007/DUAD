class Head:
    def __init__(self, eyes = 2, ears = 2, nose = 1, mouth = True):
        self.eyes = eyes
        self.ears = ears
        self.mouth = mouth
        self.nose = nose
    
    
    def hablar(self, phrase):
        if self.mouth:
            print(f"La boca está diciendo: {phrase}.")
    
    
    def __str__(self):
        phrase = f"Cabeza con {self.eyes} ojos, {self.ears} orejas, {self.mouth} boca y {self.nose} nariz."
        return phrase