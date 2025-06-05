class Movement:
    def __init__(self, category:str, movement_type:str, description:str, amount:float, date:str):
        self.category = category
        self.movement_type = movement_type
        self.description = description
        self.amount = amount
        self.date = date
    
    
    def to_dict(self) -> dict:
        return {
            "category":self.category,
            "movement_type":self.movement_type,
            "description":self.description,
            "amount":self.amount,
            "date":self.date
        }
    
    
    @staticmethod
    def from_dict(movement:dict):
        return Movement(movement["category"], movement["movement_type"], movement["description"], float(movement["amount"]), movement["date"])