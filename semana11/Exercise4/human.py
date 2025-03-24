from arm import Arm
from leg import Leg
from head import Head
from torso import Torso


class Human:
    def __init__(self, name):
        self.name = name
        self.head = Head()
        self.torso = Torso()
        self.left_arm = Arm("izquierdo")
        self.right_arm = Arm("derecho")
        self.left_leg = Leg("izquierda")
        self.right_leg = Leg("derecha")
    
    
    def presentarse(self):
        self.head.hablar(f"Hola, mi nombre es: {self.name}...")
    
    
    def respirar(self):
        self.torso.respirar()
    
    
    def agarrar_objeto(self, item):
        self.left_arm.hand.agarrar(item)
        self.right_arm.hand.agarrar(item)
    
    
    def mover_brazos(self):
        self.left_arm.mover()
        self.right_arm.mover()
    
    
    def caminar(self):
        self.left_leg.caminar()
        self.right_leg.caminar()
    
    
    def dar_paso(self):
        self.left_leg.feet.dar_paso()
        self.right_leg.feet.dar_paso()
    
    
    def __str__(self):
        phrase = f"El cuerpo de {self.name} ha realizado todas las funciones..."
        return phrase