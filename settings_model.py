from settings_manager import SettingsManager

class SettingsModel:
    def __init__(self):
        self.settings = SettingsManager()
    
    def get_settings(self):
        return self.settings
    
    def get_color_theme(self):
        return self.settings.get("color_theme")
    
    def get_font_size(self):
        return self.settings.get("font_size")
    
    def get_font_size_sp(self):
        return self.settings.get_font_size_sp()
    
    def get_font_name(self):
        return self.settings.get_font_name()
    
    def get_student_name(self):
        return self.settings.get("student_name")
    
    def get_student_id(self):
        return self.settings.get("student_id")
    
    def get_student_email(self):
        return self.settings.get("student_email")
    
    def get_academic_year(self):
        return self.settings.get("academic_year")
    
    def get_color_rgba(self):
        return self.settings.get_color_rgba()
    
    def save_settings(self, color_theme, font_size, font_family):
        self.settings.set("color_theme", color_theme)
        self.settings.set("font_size", font_size)
        self.settings.set("font_family", font_family)
        self.settings.save_settings()
    
    def save_account_settings(self, student_name, student_id, student_email, academic_year):
        self.settings.set("student_name", student_name)
        self.settings.set("student_id", student_id)
        self.settings.set("student_email", student_email)
        self.settings.set("academic_year", academic_year)
        self.settings.save_settings()

    def reset_to_default(self):
        """Reset settings to factory defaults"""
        self.settings.reset_to_default()