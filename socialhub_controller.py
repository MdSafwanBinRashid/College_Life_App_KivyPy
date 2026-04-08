from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.clock import Clock
from settings_manager import SettingsManager
from socialhub_model import SocialHubModel
import webbrowser

Builder.load_file('socialhub_view.kv')

class SocialHubView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = SettingsManager()
        self.model = SocialHubModel()
        
        Clock.schedule_once(lambda dt: self.apply_font_recursive(self, self.settings.get_font_name(), self.settings.get_font_size_sp()), 0.1)

    def apply_font_recursive(self, widget, font_name, font_size):
        """Recursively apply font to all labels and buttons"""
        if hasattr(widget, 'font_name'):
            widget.font_name = font_name
        if hasattr(widget, 'font_size'):
            if not isinstance(widget, (BoxLayout, GridLayout, ScrollView)):
                widget.font_size = font_size
        for child in widget.children:
            self.apply_font_recursive(child, font_name, font_size)

    def on_add_to_calendar(self, title):
        event = self.model.get_event(title)
        if event:
            print(f"Adding to calendar: {event['title']} on {event['date']} at {event['time']} at {event['location']}")
            url = f"https://calendar.google.com/calendar/render?action=TEMPLATE&text={event['title'].replace(' ', '+')}&location={event['location'].replace(' ', '+')}"
            webbrowser.open(url)

    def on_open_link(self, event_title):
        link = self.model.get_link(event_title)
        if link:
            print(f"Opening link for {event_title}: {link}")
            webbrowser.open(link)
        else:
            print(f"No link set for {event_title} yet")