class Hand:
    def __init__(self, side, fingers = 5):
        self.fingers = fingers
        self.side = side

    
    def agarrar(self, item):
        if self.side == "izquierdo":
            self.side = "izquierda"
            print(f"La mano {self.side} está agarrando el objeto: {item}.")
        elif self.side == "derecho":
            self.side = "derecha"
            print(f"La mano {self.side} está agarrando el objeto: {item}.")
    
    
    def __str__(self):
        phrase = ""
        if self.side == "izquierdo":
            self.side = "izquierda"
            phrase = f"La mano {self.side} tiene {self.fingers} dedos."
        elif self.side == "derecho":
            self.side = "derecha"
            phrase = f"La mano {self.side} tiene {self.fingers} dedos."
        return phrase