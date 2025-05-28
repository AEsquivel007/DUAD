class Category:
    def __init__(self, category:str):
        self.category = category
    
    
    def to_dict(self) -> dict:
        return {
            "category":self.category
        }
    
    
    @staticmethod
    def from_dict(category:dict): 
        return Category(category["category"])