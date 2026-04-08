import json
import os

class BudgetManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.file_path = "budget_data.json"
        self.default_data = {
            "total_budget": 1200.00,
            "category_estimates": {
                "Food": 200.00,
                "Rent": 500.00,
                "Books": 150.00,
                "Entertainment": 100.00,
                "Transport": 250.00
            },
            "transactions": [
                {"date": "02/03/26", "category": "Food", "amount": 45.00},
                {"date": "02/04/26", "category": "Transport", "amount": 12.50},
                {"date": "02/05/26", "category": "Books", "amount": 89.99},
                {"date": "02/06/26", "category": "Entertainment", "amount": 25.00},
                {"date": "02/07/26", "category": "Food", "amount": 32.50},
                {"date": "02/08/26", "category": "Transport", "amount": 8.75},
                {"date": "02/09/26", "category": "Rent", "amount": 500.00},
                {"date": "02/10/26", "category": "Books", "amount": 45.99},
                {"date": "02/11/26", "category": "Entertainment", "amount": 60.00},
                {"date": "02/12/26", "category": "Food", "amount": 78.25},
                {"date": "02/13/26", "category": "Transport", "amount": 15.00},
                {"date": "02/14/26", "category": "Entertainment", "amount": 35.00}
            ]
        }
        self.data = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    return json.load(f)
            except:
                return self.default_data.copy()
        else:
            return self.default_data.copy()
    
    def save_data(self):
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.data, f, indent=2)
        except:
            print("Failed to save budget data")
    
    def get_total_budget(self):
        return self.data["total_budget"]
    
    def set_total_budget(self, new_budget):
        self.data["total_budget"] = new_budget
        self.save_data()
    
    def get_category_estimates(self):
        return self.data.get("category_estimates", self.default_data["category_estimates"])
    
    def set_category_estimate(self, category, amount):
        if category in self.data["category_estimates"]:
            self.data["category_estimates"][category] = amount
            self.save_data()
    
    def get_transactions(self):
        return self.data["transactions"]
    
    def add_transaction(self, date, category, amount):
        self.data["transactions"].append({"date": date, "category": category, "amount": amount})
        self.save_data()
    
    def delete_transaction(self, index):
        if 0 <= index < len(self.data["transactions"]):
            del self.data["transactions"][index]
            self.save_data()
            return True
        return False