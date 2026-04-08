from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from settings_model import SettingsModel

Builder.load_file('settings_view.kv')

class SettingsView(BoxLayout):
    sample_text = StringProperty("Sample text: The quick brown fox jumps.")
    current_font_size = NumericProperty(28)
    current_font_name = StringProperty('Roboto')
    current_theme = StringProperty("Midnight Blue")
    
    student_name = StringProperty("")
    student_id = StringProperty("")
    student_email = StringProperty("")
    academic_year = StringProperty("")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = SettingsModel()
        self.load_current_settings()
        self.update_sample_text()
        
        # Apply saved font to Settings tab itself
        Clock.schedule_once(lambda dt: self.apply_font_recursive(self, self.model.get_font_name(), self.model.get_font_size_sp()), 0.2)
    
    def apply_font_recursive(self, widget, font_name, font_size):
        """Recursively apply font to all labels and buttons"""
        if hasattr(widget, 'font_name'):
            widget.font_name = font_name
        if hasattr(widget, 'font_size'):
            if not isinstance(widget, (BoxLayout, GridLayout, ScrollView)):
                try:
                    widget.font_size = font_size
                except:
                    pass
        for child in widget.children:
            self.apply_font_recursive(child, font_name, font_size)
    
    def load_current_settings(self):
        """Load current settings into UI"""
        self.current_theme = self.model.get_color_theme()
        self.current_font_size = self.model.get_font_size_sp()
        self.current_font_name = self.model.get_font_name()
        
        self.student_name = self.model.get_student_name()
        self.student_id = self.model.get_student_id()
        self.student_email = self.model.get_student_email()
        self.academic_year = self.model.get_academic_year()
        
        if hasattr(self.ids, 'color_spinner'):
            self.ids.color_spinner.text = self.current_theme
        if hasattr(self.ids, 'size_spinner'):
            size_text = self.model.get_settings().get("font_size")
            self.ids.size_spinner.text = size_text
        if hasattr(self.ids, 'family_spinner'):
            family_text = self.model.get_settings().get("font_family")
            self.ids.family_spinner.text = family_text
    
    def on_change_color_theme(self, theme):
        self.current_theme = theme
        self.update_sample_text()
    
    def on_change_font_size(self, size):
        self.current_font_size = self.model.get_font_size_sp()
        self.update_sample_text()
    
    def on_change_font_family(self, family):
        self.current_font_name = self.get_font_value(family)
        self.update_sample_text()
    
    def get_font_value(self, family):
        fonts = {
            "Georgia": "Georgia",
            "Roboto": "Roboto",
        }
        return fonts.get(family, "Roboto")
    
    def on_save_settings(self):
        """Save all settings and apply globally"""
        self.model.save_settings(
            self.current_theme,
            self.ids.size_spinner.text,
            self.ids.family_spinner.text
        )
        
        # Apply color theme to main layout
        self.apply_color_theme()
        
        # Apply font settings to current tab
        self.apply_fonts_to_current_tab()
        
        print("Settings saved! Changes will apply when you reopen tabs.")
    
    def apply_fonts_to_current_tab(self):
        """Apply current font settings to the currently visible tab"""
        font_name = self.model.get_font_name()
        font_size = self.model.get_font_size_sp()
        
        # Apply fonts to current content area
        parent = self.parent
        while parent:
            if hasattr(parent, 'ids') and 'content_area' in parent.ids:
                content_area = parent.ids.content_area
                if content_area.children:
                    current_tab = content_area.children[0]
                    self.apply_font_recursive(current_tab, font_name, font_size)
                break
            parent = parent.parent
    
    def apply_color_theme(self):
        """Apply color theme to main app background"""
        main_layout = None
        parent = self.parent
        while parent:
            if hasattr(parent, 'ids') and 'content_area' in parent.ids:
                main_layout = parent
                break
            parent = parent.parent
        
        if main_layout:
            color = self.model.get_color_rgba()
            main_layout.canvas.before.clear()
            with main_layout.canvas.before:
                Color(*color)
                Rectangle(pos=main_layout.pos, size=main_layout.size)
            
            def update_rect(instance, value):
                if main_layout.canvas.before.children:
                    main_layout.canvas.before.children[-1].pos = instance.pos
                    main_layout.canvas.before.children[-1].size = instance.size
            
            main_layout.bind(pos=update_rect, size=update_rect)
    
    def update_sample_text(self):
        self.sample_text = f"The quick brown fox jumps."
        if hasattr(self.ids, 'sample_label'):
            self.ids.sample_label.font_size = self.current_font_size
            self.ids.sample_label.font_name = self.current_font_name

    def on_save_account_settings(self):
        self.model.save_account_settings(
            self.ids.name_input.text,
            self.ids.id_input.text,
            self.ids.email_input.text,
            self.ids.year_spinner.text
        )
        print("Account settings saved!")

        