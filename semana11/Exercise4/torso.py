class Torso:
    def __init__(self, heart = True, lungs = 2, ribs = 2, stomach = 2):
        self.heart = heart
        self.lungs = lungs
        self.ribs = ribs
        self.stomatch = stomach
    
    
    def breathe(self):
        print("Breathing...")
    
    
    def __str__(self):
        phrase = f"My torso has {self.heart} corazón, {self.lungs} lungs, {self.ribs} ribs and {self.stomatch} estomach."
        return phrase
