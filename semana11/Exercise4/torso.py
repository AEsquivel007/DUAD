class Torso:
    def __init__(self, heart = True, lungs = 2, ribs = 2, stomach = 2):
        self.heart = heart
        self.lungs = lungs
        self.ribs = ribs
        self.stomatch = stomach
    
    
    def respirar(self):
        print("Respirando...")
    
    
    def __str__(self):
        phrase = f"El torso del cuerpo tiene {self.heart} corazón, {self.lungs} pulmones, {self.ribs} costillas y {self.stomatch} estómago."
        return phrase
