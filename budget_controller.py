from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.clock import Clock
from settings_manager import SettingsManager
from budget_model import BudgetModel

Builder.load_file('budget_view.kv')

class BudgetView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = SettingsManager()
        self.model = BudgetModel()
        
        Clock.schedule_once(lambda dt: self.refresh_all(), 0.1)
        Clock.schedule_once(lambda dt: self.apply_font_recursive(self, self.settings.get_font_name(), self.settings.get_font_size_sp()), 0.2)
    
    def refresh_all(self):
        self.update_budget_cards()
        self.refresh_transactions()
        self.refresh_category_overview()
    
    def update_budget_cards(self):
        total = self.model.get_total_budget()
        spent = self.model.get_spent_total()
        remaining = self.model.get_remaining()
        self.ids.spent_amount.text = f"${spent:.2f}"
        self.ids.remaining_amount.text = f"${remaining:.2f}"
        if hasattr(self.ids, 'total_budget_label'):
            self.ids.total_budget_label.text = f"${total:.2f}"
    
    def refresh_transactions(self):
        self.ids.transactions_list.clear_widgets()
        for idx, t in enumerate(reversed(self.model.get_transactions())):
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=45, spacing=5)
            row.add_widget(Label(text=t['date'], size_hint_x=0.25, font_size='11sp', color=(0,0,0,1)))
            row.add_widget(Label(text=t['category'], size_hint_x=0.3, font_size='11sp', color=(0,0,0,1)))
            row.add_widget(Label(text=f"${t['amount']:.2f}", size_hint_x=0.3, font_size='11sp', color=(0,0,0,1), halign='right'))
            
            # Delete button
            del_btn = Button(text='x', size_hint_x=0.07, background_normal='', background_color=(0.8, 0.2, 0.2, 1), font_size='14sp', color=(1,1,1,1))
            del_btn.bind(on_press=lambda instance, idx=idx: self.delete_transaction(idx))
            row.add_widget(del_btn)
            
            self.ids.transactions_list.add_widget(row)
    
    def delete_transaction(self, index):
        original_index = len(self.model.get_transactions()) - 1 - index
        if self.model.delete_transaction(original_index):
            self.update_budget_cards()
            self.refresh_transactions()
    
    def on_add_transaction(self):
        date = self.ids.transaction_date.text
        category = self.ids.transaction_category.text
        amount_text = self.ids.transaction_amount.text
        if date and category != "Select Category" and amount_text:
            amount = float(amount_text)
            self.model.add_transaction(date, category, amount)
            self.update_budget_cards()
            self.refresh_transactions()
            
            self.ids.transaction_date.text = ""
            self.ids.transaction_category.text = "Select Category"
            self.ids.transaction_amount.text = ""
    
    def on_set_budget(self):
        """Called when user sets a new monthly budget"""
        try:
            new_budget = float(self.ids.new_budget_input.text)
            if new_budget > 0:
                self.model.set_total_budget(new_budget)
                self.update_budget_cards()
                self.ids.new_budget_input.text = ""
        except:
            pass
    
    def apply_font_recursive(self, widget, font_name, font_size):
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

    def refresh_category_overview(self):
        estimates = self.model.get_category_estimates()
        total = self.model.get_total_budget()
    
        # Update amount labels
        self.ids.food_amount.text = f"${estimates['Food']:.2f}"
        self.ids.rent_amount.text = f"${estimates['Rent']:.2f}"
        self.ids.books_amount.text = f"${estimates['Books']:.2f}"
        self.ids.entertainment_amount.text = f"${estimates['Entertainment']:.2f}"
        self.ids.transport_amount.text = f"${estimates['Transport']:.2f}"
    
        # Update progress bars
        if total > 0:
            self.ids.food_bar.value = (estimates['Food'] / total) * 100
            self.ids.rent_bar.value = (estimates['Rent'] / total) * 100
            self.ids.books_bar.value = (estimates['Books'] / total) * 100
            self.ids.entertainment_bar.value = (estimates['Entertainment'] / total) * 100
            self.ids.transport_bar.value = (estimates['Transport'] / total) * 100

    def on_save_category(self, category):
        try:
            input_id = f"{category.lower()}_input"
            new_amount = float(self.ids[input_id].text)
            if new_amount >= 0:
                self.model.set_category_estimate(category, new_amount)
                self.refresh_category_overview()
                elf.ids[input_id].text = ""
        except:
            pass