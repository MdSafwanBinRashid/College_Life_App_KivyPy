class ScheduleModel:
    def __init__(self):
        self.schedule_data = {
            "Monday": [
                {"course": "CSC102", "time": "10:00 - 11:30 AM"},
                {"course": "MAT327", "time": "1:00 - 2:30 PM"}
            ],
            "Tuesday": [
                {"course": "PHY111", "time": "9:00 - 10:30 AM"},
                {"course": "CSC327", "time": "11:00 - 12:30 PM"},
                {"course": "ENG203", "time": "2:00 - 3:30 PM"}
            ],
            "Wednesday": [
                {"course": "CSC102", "time": "10:00 - 11:30 AM"},
                {"course": "MAT327", "time": "1:00 - 2:30 PM"},
            ],
            "Thursday": [
                {"course": "CSC411", "time": "9:00 - 10:30 AM"},
                {"course": "CHE340", "time": "11:00 - 12:30 PM"},
            ],
            "Friday": [
                {"course": "CSC327", "time": "9:00 - 10:30 AM"},
            ]
        }
        self.days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    def get_schedule_data(self):
        return self.schedule_data
    
    def get_days_order(self):
        return self.days_order
    
    def add_class(self, course, day, time):
        if course and day and time:
            day = day.capitalize()
            if day not in self.schedule_data:
                self.schedule_data[day] = []
            self.schedule_data[day].append({"course": course, "time": time})
            return True
        return False