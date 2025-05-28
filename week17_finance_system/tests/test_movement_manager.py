import unittest
from classes.movement import Movement
from managers.movement_manager import MovementManager
import csv
import os

test_movement_file_path = "tests/test_movements.csv"

class TestMovementManager(unittest.TestCase):
    
    def setUp(self):
        self.manager = MovementManager(test_movement_file_path)
        self.manager.movements = []
    
    
    def tearDown(self):
        if os.path.exists(test_movement_file_path):
            os.remove(test_movement_file_path)
    
    
    def test_add_movement(self):
        movement = Movement("Food", "Expense", "5 Stars Restaurant", 500, "2025-5-28")
        self.manager.add_movement(movement)
        movement = self.manager.movements[0]
        movement_to_assert = [movement.category, movement.movement_type, movement.description, movement.amount, movement.date]
        self.assertEqual(movement_to_assert, ["Food", "Expense", "5 Stars Restaurant", 500, "2025-5-28"])
    
    
    def test_get_movements_as_rows(self):
        fieldnames = ["category", "movement_type", "description", "amount", "date"]
        
        with open(test_movement_file_path, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"category":"Technology", "movement_type":"Expense","description":"Smart TV","amount":2590.50,"date":"2025-5-28"})
            writer.writerow({"category":"Housing", "movement_type":"Income","description":"Rent Payment","amount":1500,"date":"2025-5-28"})
        
        self.manager.load_movements()
        movements = self.manager.get_movements_as_rows()
        expected_movements = [
            ["Technology","Expense","Smart TV",2590.50,"2025-5-28"], 
            ["Housing","Income","Rent Payment",1500,"2025-5-28"]
        ]
        
        self.assertEqual(movements, expected_movements)
    
    
    def test_movement_to_dict(self):
        movement = Movement("Vehicles", "Expense", "Toyota Prado 2025", 85000, "2025-5-28")
        movement_as_dict = movement.to_dict()
        self.assertEqual(movement_as_dict, {"category":"Vehicles", "movement_type":"Expense","description":"Toyota Prado 2025","amount":85000,"date":"2025-5-28"})
        
    
    def test_get_movements_as_rows_without_movements(self):
        movements = self.manager.get_movements_as_rows()
        self.assertEqual(movements, [])
    
    if __name__ == "__main__":
        unittest.main()
