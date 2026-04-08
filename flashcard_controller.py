from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.properties import NumericProperty, BooleanProperty, StringProperty
from kivy.clock import Clock
from settings_manager import SettingsManager
from flashcard_model import FlashcardModel

Builder.load_file('flashcard_view.kv')

class FlashcardView(BoxLayout):
    current_index = NumericProperty(0)
    total_cards = NumericProperty(0)
    is_flipped = BooleanProperty(False)
    current_question = StringProperty("")
    current_answer = StringProperty("")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = SettingsManager()
        self.model = FlashcardModel()
        
        self.current_index = self.model.get_current_index()
        self.total_cards = self.model.get_total_cards()
        self.update_card_display()
        
        # Apply font settings after UI is built
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
    
    def update_card_display(self):
        card = self.model.get_current_card()
        if card:
            self.current_question = card["question"]
            self.current_answer = card["answer"]
            self.is_flipped = False
    
    def on_flip_card(self):
        self.is_flipped = not self.is_flipped
    
    def on_next_card(self):
        if self.model.next_card():
            self.current_index = self.model.get_current_index()
            self.update_card_display()
    
    def on_previous_card(self):
        if self.model.previous_card():
            self.current_index = self.model.get_current_index()
            self.update_card_display()
    
    def on_add_card(self):
        question = self.ids.new_question.text.strip()
        answer = self.ids.new_answer.text.strip()
        if self.model.add_card(question, answer):
            self.current_index = self.model.get_current_index()
            self.total_cards = self.model.get_total_cards()
            self.update_card_display()
            # Clear inputs
            self.ids.new_question.text = ""
            self.ids.new_answer.text = ""
            
    def on_delete_card(self):
        if self.model.delete_current_card():
            self.current_index = self.model.get_current_index()
            self.total_cards = self.model.get_total_cards()
            self.update_card_display()
            print("Card deleted.")