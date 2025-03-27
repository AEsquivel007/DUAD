class Head:
    def __init__(self, eyes = 2, ears = 2, nose = 1, mouth = 1):
        self.eyes = eyes
        self.ears = ears
        self.mouth = mouth
        self.nose = nose
    
    
    def speak(self, phrase):
        if self.mouth:
            print(f"My mouth is saying: '{phrase}.'")
    
    
    def __str__(self):
        phrase = f"My head has {self.eyes} eyes, {self.ears} ears, {self.mouth} mouth and {self.nose} nose."
        return phrase