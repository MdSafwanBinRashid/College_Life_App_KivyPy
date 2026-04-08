import json
import os

class DashboardManager:
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
        self.file_path = "dashboard_data.json"
        self.default_data = {
            "tasks": [
                {"task": "Project Milestone 2", "deadline": "02/18/26"},
                {"task": "Video Assignment 4.2", "deadline": "02/20/26"},
                {"task": "Manuscript Submission", "deadline": "02/21/26"},
                {"task": "Group Presentation", "deadline": "02/22/26"},
                {"task": "Career Fair 2026", "deadline": "02/25/26"},
                {"task": "Spring Festival", "deadline": "02/26/26"},
                {"task": "Hackathon Registration", "deadline": "03/05/26"},
                {"task": "Advising Meeting", "deadline": "03/19/26"}
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
            print("Failed to save dashboard data")
    
    def get_tasks(self):
        return self.data["tasks"]
    
    def add_task(self, task_name, deadline):
        if task_name and deadline:
            self.data["tasks"].append({"task": task_name, "deadline": deadline})
            self.save_data()
            return True
        return False
    
    def delete_task(self, index):
        if 0 <= index < len(self.data["tasks"]):
            del self.data["tasks"][index]
            self.save_data()
            return True
        return False
    