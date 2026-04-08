import json
import os

class SettingsManager:
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
        self.settings_file = "user_settings.json"
        self.default_settings = {
            "color_theme": "Midnight Blue",
            "font_size": "Medium",
            "font_family": "Roboto",
            "student_name": "Md Safwan Bin Rashid",
            "student_id": "w10188533",
            "student_email": "MdSafwanBin.Rashid@usm.edu",
            "academic_year": "Sophomore"
        }
        self.current_settings = self.default_settings.copy()
        self.load_settings()
    
    def load_settings(self):
        """Load settings from file if exists"""
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    saved = json.load(f)
                    self.current_settings.update(saved)
                print(f"Settings loaded: {self.current_settings}")
            except:
                print("Failed to load settings, using defaults")
    
    def save_settings(self):
        """Save current settings to file"""
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(self.current_settings, f)
            print(f"Settings saved: {self.current_settings}")
        except:
            print("Failed to save settings")
    
    def get(self, key):
        return self.current_settings.get(key, self.default_settings.get(key))
    
    def set(self, key, value):
        self.current_settings[key] = value
    
    def get_color_rgba(self):
        """Return RGBA color for current theme"""
        theme = self.get("color_theme")
        colors = {
            "Midnight Blue": (0, 0, 0.15, 1),
            "Ocean Breeze": (0.1, 0.5, 0.6, 1),
            "Hot Pink": (0.8, 0.2, 0.6, 1),
            "Forest Green": (0, 0.4, 0.2, 1),
            "Amber Glow": (0.8, 0.5, 0.1, 1)
        }
        return colors.get(theme, (0, 0, 0.15, 1))
    
    def get_font_size_sp(self):
        """Return font size in sp"""
        size = self.get("font_size")
        sizes = {
            "Small": 26,
            "Medium": 28,
            "Large": 30
        }
        return sizes.get(size, 28)
    
    def get_font_name(self):
        """Return font name"""
        family = self.get("font_family")
        fonts = {
            "Georgia": "Georgia",
            "Roboto": "Roboto",
        }
        return fonts.get(family, "Roboto")
    