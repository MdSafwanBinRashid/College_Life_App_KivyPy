from budget_manager import BudgetManager

class BudgetModel:
    def __init__(self):
        self.manager = BudgetManager()
    
    def get_total_budget(self):
        return self.manager.get_total_budget()
    
    def set_total_budget(self, new_budget):
        self.manager.set_total_budget(new_budget)
    
    def get_category_estimates(self):
        return self.manager.get_category_estimates()
    
    def set_category_estimate(self, category, amount):
        self.manager.set_category_estimate(category, amount)
    
    def get_transactions(self):
        return self.manager.get_transactions()
    
    def get_spent_total(self):
        return sum(t["amount"] for t in self.manager.get_transactions())
    
    def get_remaining(self):
        return self.get_total_budget() - self.get_spent_total()
    
    def add_transaction(self, date, category, amount):
        self.manager.add_transaction(date, category, amount)
    
    def delete_transaction(self, index):
        return self.manager.delete_transaction(index)