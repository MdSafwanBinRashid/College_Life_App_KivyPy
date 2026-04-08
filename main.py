from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from dashboard_controller import DashboardView
from settings_manager import SettingsManager
from schedule_controller import ScheduleView
from socialhub_controller import SocialHubView
from budget_controller import BudgetView
from flashcard_controller import FlashcardView
from settings_controller import SettingsView

Window.size = (330, 650)

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = SettingsManager()
        self.apply_saved_theme()

        Clock.schedule_once(lambda dt: self.update_content("Dashboard"), 0.1)
    
    def apply_saved_theme(self):
        """Apply saved color theme to main layout"""
        color = self.settings.get_color_rgba()
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*color)
            Rectangle(pos=self.pos, size=self.size)
        
        def update_rect(instance, value):
            if self.canvas.before.children:
                self.canvas.before.children[-1].pos = instance.pos
                self.canvas.before.children[-1].size = instance.size
        
        self.bind(pos=update_rect, size=update_rect)
    
    def toggle_menu(self):
        menu = self.ids.menu_overlay
        
        if menu.height == 0:
            menu.height = 500
            menu.opacity = 1
        else:
            menu.height = 0
            menu.opacity = 0

    def select_tab(self, tab_name):
        self.toggle_menu()  # Close menu
        self.update_content(tab_name)

    def update_content(self, tab_name):
        self.ids.content_area.clear_widgets()
        
        if tab_name == "Dashboard":
            dashboard_widget = DashboardView()
            self.ids.content_area.add_widget(dashboard_widget)
        
        elif tab_name == "Schedule":
            schedule_widget = ScheduleView()
            self.ids.content_area.add_widget(schedule_widget)
        
        elif tab_name == "Budgeting":
            budgeting_widget = BudgetView()
            self.ids.content_area.add_widget(budgeting_widget)

        elif tab_name == "Social Hub":
            social_widget = SocialHubView()
            self.ids.content_area.add_widget(social_widget)

        elif tab_name == "Flashcards":
            flashcard_widget = FlashcardView()
            self.ids.content_area.add_widget(flashcard_widget)

        elif tab_name == "Settings":
            settings_widget = SettingsView()
            self.ids.content_area.add_widget(settings_widget)

        else:
            placeholder = Label(text=f"{tab_name} Content - Coming Soon", size_hint_y=1, font_size='12sp')
            self.ids.content_area.add_widget(placeholder)

    def apply_font_to_widget(self, widget, font_name, font_size):
        """Recursively apply font to all labels and buttons"""
        if hasattr(widget, 'font_name'):
            widget.font_name = font_name
        if hasattr(widget, 'font_size'):
            if not isinstance(widget, (BoxLayout, GridLayout, ScrollView)):
                widget.font_size = font_size
        
        for child in widget.children:
            self.apply_font_to_widget(child, font_name, font_size)

    def update_menu_color(self):
        color = self.settings.get_color_rgba()
        menu = self.ids.menu_overlay
        if menu.canvas.before.children:
            menu.canvas.before.children[-2].rgba = color 

class CollegeLifeApp(App):
    def build(self):
        root = MainLayout()
        root.app = self
        return root

if __name__ == '__main__':
    CollegeLifeApp().run()