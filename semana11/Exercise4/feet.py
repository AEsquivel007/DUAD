class Feet:
    def __init__(self, side, toes = 5):
        self.toes = toes
        self.side = side
    
    
    def dar_paso(self):
        
        if self.side == "izquierda":
            self.side = "izquierdo"
            print(f"El pie {self.side} ha dado un paso.")
        elif self.side == "derecha":
            self.side = "derecho"
            print(f"El pie {self.side} ha dado un paso.")
    
    
    def __str__(self):
        phrase = ""
        if self.side == "izquierda":
            self.side = "izquierdo"
            phrase = f"El pie {self.side} tiene {self.toes} dedos."
        elif self.side == "derecha":
            self.side = "derecho"
            phrase = f"El pie {self.side} tiene {self.toes} dedos."
        return phrase