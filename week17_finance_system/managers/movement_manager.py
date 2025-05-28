from classes.movement import Movement
from helpers.csv_helper import validate_if_file_exists
import csv

class MovementManager:
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.movements:list[Movement] = []
    
    
    def load_movements(self):
        file_exists = validate_if_file_exists(self.filepath)
        
        if not file_exists:
            self.movements = []
            return
        with open(self.filepath, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.movements = [Movement.from_dict(movement) for movement in reader]
    
    
    def save_movements(self):
        fieldnames = ["category", "movement_type", "description", "amount", "date"]
        
        with open(self.filepath, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            
            for movement in self.movements:
                writer.writerow(movement.to_dict())
    
    
    def add_movement(self, movement:Movement):
        self.movements.append(movement)
        self.save_movements()
    
    
    def modify_movement(self, index, movement:Movement):
        if index >= 0 and index < len(self.movements):
            self.movements[index] = movement
            self.save_movements()
    
    
    def delete_movement(self, index):
        if index >= 0 and index < len(self.movements):
            del self.movements[index]
            self.save_movements()
    
    
    def get_movements_as_rows(self):
        return [[movement.category, movement.movement_type, movement.description, movement.amount, movement.date] for movement in self.movements]