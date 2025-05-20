from classes.category import Category
from helpers.csv_helper import validate_if_file_exists
import csv

class CategoryManager:
    def __init__(self, filepath:str):
        self.filepath = filepath
        self.categories: list[Category] = []
    
    
    def load_categories(self):
        file_exists = validate_if_file_exists
        
        if not file_exists(self.filepath):
            self.categories = []
            return
        with open(self.filepath, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.categories = [Category.from_dict(category) for category in reader]
    
    
    def add_category(self, category: Category):
        self.categories.append(category)
    
    
    def save_categories(self):
        fieldnames = ["category"]
        
        with open(self.filepath, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for category in self.categories:
                writer.writerow(category.to_dict())
    
    
    def get_categories_as_rows(self):
        return [[category.category] for category in self.categories]