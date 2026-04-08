from budget_manager import BudgetManager
from dashboard_manager import DashboardManager

class DashboardModel:
    def __init__(self):
        self.budget_manager = BudgetManager()
        self.dashboard_manager = DashboardManager()
        
        self.gpa = {
            "cgpa": 3.91,
            "credits": 55,
            "deans_list": "Eligible"
        }
    
    def get_tasks(self):
        return self.dashboard_manager.get_tasks()
    
    def add_task(self, task_name, deadline):
        return self.dashboard_manager.add_task(task_name, deadline)
    
    def delete_task(self, index):
        return self.dashboard_manager.delete_task(index)
    
    def get_gpa_data(self):
        return self.gpa
    
    def get_budget_data(self):
        total = self.budget_manager.get_total_budget()
        spent = sum(t["amount"] for t in self.budget_manager.get_transactions())
        remaining = total - spent
        progress = remaining / total if total > 0 else 0
        return {
            "total": total,
            "spent": spent,
            "remaining": remaining,
            "progress": progress
        }
