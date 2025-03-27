from arm import Arm
from leg import Leg
from head import Head
from torso import Torso


class Human:
    def __init__(self, name):
        self.name = name
        self.head = Head()
        self.torso = Torso()
        self.left_arm = Arm("left")
        self.right_arm = Arm("right")
        self.left_leg = Leg("left")
        self.right_leg = Leg("right")
    
    
    def introduce(self):
        self.head.speak(f"Hello, my name is: {self.name}...")
    
    
    def breathe(self):
        self.torso.breathe()
    
    
    def grab_object(self, item):
        self.left_arm.hand.grab(item)
        self.right_arm.hand.grab(item)
    
    
    def move_arms(self):
        self.left_arm.move()
        self.right_arm.move()
    
    
    def walk(self):
        self.left_leg.walk()
        self.right_leg.walk()
    
    
    def step(self):
        self.left_leg.feet.step()
        self.right_leg.feet.step()
    
    
    def __str__(self):
        phrase = f"{self.name}'s body has fulfilled all its functions..."
        return phrase