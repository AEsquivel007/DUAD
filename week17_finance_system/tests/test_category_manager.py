import unittest
from classes.category import Category 
from managers.category_manager import CategoryManager
import csv
import os


test_category_file_path = "tests/test_categories.csv"


class TestCategoryManager(unittest.TestCase):
    
    def setUp(self):
        self.manager = CategoryManager(test_category_file_path)
        self.manager.categories = []
    
    
    def tearDown(self):
        if os.path.exists(test_category_file_path):
            os.remove(test_category_file_path)
    
    
    def test_load_categories(self):
        with open(test_category_file_path, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["category"])
            writer.writeheader()
            writer.writerow({"category":"Technology"})
            writer.writerow({"category":"Food"})
        
        self.manager.load_categories()
        categories = self.manager.get_categories()
        self.assertEqual(categories, ["Technology", "Food"])
    
    
    def test_add_category(self):
        category = Category("Education")
        self.manager.add_category(category)
        
        self.assertEqual(self.manager.categories[0].category, "Education")
        
        with open(test_category_file_path, mode="r", newline='', encoding="utf-8") as file:
            reader = list(csv.DictReader(file))
            self.assertEqual(reader[0]["category"], "Education")
    
    
    def test_category_to_dict(self):
        category = Category("Technology")
        category_as_dict = category.to_dict()
        self.assertEqual(category_as_dict, {"category":"Technology"})
    
    
    def test_get_categories_without_categories(self):
        categories = self.manager.get_categories()
        self.assertEqual(categories, [])
    
    
    if __name__ == '__main__':
        unittest.main()