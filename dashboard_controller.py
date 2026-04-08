from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from settings_manager import SettingsManager
from dashboard_model import DashboardModel

Builder.load_file('dashboard_view.kv')

class DashboardView(BoxLayout):
    cgpa = StringProperty("3.91")
    credits = StringProperty("55")
    deans_list = StringProperty("Eligible")
    total_budget = NumericProperty(1200.0)
    remaining = NumericProperty(676.50)
    budget_progress = NumericProperty(0.43625)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = SettingsManager()
        self.model = DashboardModel()
        
        gpa_data = self.model.get_gpa_data()
        self.cgpa = str(gpa_data["cgpa"])
        self.credits = str(gpa_data["credits"])
        self.deans_list = gpa_data["deans_list"]
        
        # Apply font settings after UI is built
        Clock.schedule_once(lambda dt: self.refresh_todo_list(), 0.1)
        Clock.schedule_once(lambda dt: self.refresh_budget_display(), 0.15)
        Clock.schedule_once(lambda dt: self.apply_font_recursive(self, self.settings.get_font_name(), self.settings.get_font_size_sp()), 0.2)
    
    def refresh_todo_list(self):
        self.ids.todo_list.clear_widgets()
        for idx, task in enumerate(self.model.get_tasks()):
            row = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
            
            task_label = Label(
                text=task["task"],
                size_hint_x=0.55,
                font_size='13sp',
                halign='left',
                valign='middle',
                color=(0, 0, 0, 0.85)
            )
            task_label.bind(width=lambda inst, val: setattr(inst, 'text_size', (val, None)))
            
            deadline_label = Label(
                text=task["deadline"],
                size_hint_x=0.28,
                font_size='12sp',
                halign='right',
                valign='middle',
                color=(0.5, 0.1, 0.1, 1),
                bold=True
            )
            deadline_label.bind(width=lambda inst, val: setattr(inst, 'text_size', (val, None)))
            
            # Delete button
            del_btn = Button(
                text='x',
                size_hint_x=0.07,
                background_normal='',
                background_color=(0.5, 0.5, 0.5, 1),
                font_size='14sp',
                color=(1, 1, 1, 1)
            )
            del_btn.bind(on_press=lambda instance, i=idx: self.delete_task(i))
            
            row.add_widget(task_label)
            row.add_widget(deadline_label)
            row.add_widget(del_btn)
            
            self.ids.todo_list.add_widget(row)
    
    def delete_task(self, index):
        if self.model.delete_task(index):
            self.refresh_todo_list()
    
    def on_add_task(self):
        task_name = self.ids.task_input.text.strip()
        deadline = self.ids.deadline_input.text.strip()
        
        if self.model.add_task(task_name, deadline):
            self.refresh_todo_list()
            self.ids.task_input.text = ""
            self.ids.deadline_input.text = ""
    
    def refresh_budget_display(self):
        budget_data = self.model.get_budget_data()
        self.total_budget = budget_data["total"]
        self.remaining = budget_data["remaining"]
        self.budget_progress = budget_data["progress"]
        
        if hasattr(self.ids, 'total_budget_label'):
            self.ids.total_budget_label.text = f"${self.total_budget:.2f}"
        if hasattr(self.ids, 'remaining_label'):
            self.ids.remaining_label.text = f"${self.remaining:.2f}"
        if hasattr(self.ids, 'budget_progress'):
            self.ids.budget_progress.value = self.budget_progress
    
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