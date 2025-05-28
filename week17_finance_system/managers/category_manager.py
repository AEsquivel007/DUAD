from classes.category import Category
from helpers.csv_helper import validate_if_file_exists
import csv

class CategoryManager:
    
    def __init__(self, filepath:str):
        self.filepath = filepath
        self.categories: list[Category] = []
    
    
    def load_categories(self):
        file_exists = validate_if_file_exists(self.filepath)
        
        if not file_exists:
            self.categories = []
            return
        with open(self.filepath, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.categories = [Category.from_dict(category) for category in reader]
        return self.categories
    
    
    def save_categories(self):
        fieldnames = ["category"]
        
        with open(self.filepath, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for category in self.categories:
                writer.writerow(category.to_dict())
    
    
    def add_category(self, category: Category):
        self.categories.append(category)
        self.save_categories()
    
    
    def modify_category(self, index, category:Category):
        if index >= 0 and index < len(self.categories):
            self.categories[index] = category
            self.save_categories()
    
    
    def delete_category(self, index):
        if index >= 0 and index < len(self.categories):
            del self.categories[index]
            self.save_categories()
    
    def get_categories_as_rows(self):
        return [[category.category] for category in self.categories]
    
    
    def get_categories(self):
        return [category.category for category in self.categories]