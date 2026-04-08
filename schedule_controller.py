from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from settings_manager import SettingsManager
from schedule_model import ScheduleModel

Builder.load_file('schedule_view.kv')

class ScheduleView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = SettingsManager()
        self.model = ScheduleModel()
        
        # Apply font settings
        Clock.schedule_once(lambda dt: self.apply_font_recursive(self, self.settings.get_font_name(), self.settings.get_font_size_sp()), 0.1)
        Clock.schedule_once(lambda dt: self.refresh_display(), 0.1)
    
    def apply_font_recursive(self, widget, font_name, font_size):
        if hasattr(widget, 'font_name'):
            widget.font_name = font_name
        if hasattr(widget, 'font_size'):
            if not isinstance(widget, (BoxLayout, GridLayout, ScrollView)):
                widget.font_size = font_size
        for child in widget.children:
            self.apply_font_recursive(child, font_name, font_size)
    
    def on_add_class(self):
        course = self.ids.course_input.text
        day = self.ids.day_input.text
        time = self.ids.time_input.text
        
        if self.model.add_class(course, day, time):
            self.refresh_display()
            self.ids.course_input.text = ""
            self.ids.day_input.text = ""
            self.ids.time_input.text = ""
    
    def refresh_display(self):
        schedule_list = self.ids.schedule_list
        schedule_list.clear_widgets()
        
        for day in self.model.get_days_order():
            if day in self.model.get_schedule_data() and self.model.get_schedule_data()[day]:
                day_section = BoxLayout(orientation='vertical', size_hint_y=None, 
                                       height=50 + len(self.model.get_schedule_data()[day]) * 55, spacing=5)
                
                header = BoxLayout(orientation='horizontal', size_hint_y=None, height=45)
                with header.canvas.before:
                    Color(0, 0, 0.4, 1)
                    Rectangle(pos=header.pos, size=header.size)
                
                def update_header_bg(instance, value):
                    if instance.canvas.before.children:
                        instance.canvas.before.children[-1].pos = instance.pos
                        instance.canvas.before.children[-1].size = instance.size
                
                header.bind(pos=update_header_bg, size=update_header_bg)
                
                day_label = Label(text=day, font_size='16sp', bold=True, color=(1,1,1,1), 
                                 halign='left', valign='middle', size_hint_x=0.8)
                day_label.bind(width=lambda inst, val: setattr(inst, 'text_size', (val, None)))
                header.add_widget(day_label)
                day_section.add_widget(header)
                
                for class_item in self.model.get_schedule_data()[day]:
                    class_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
                    
                    course_label = Label(text=class_item["course"], size_hint_x=0.55, font_size='14sp',
                                        halign='left', valign='middle', color=(0,0,0,0.85))
                    course_label.bind(width=lambda inst, val: setattr(inst, 'text_size', (val, None)))
                    
                    time_label = Label(text=class_item["time"], size_hint_x=0.45, font_size='12sp',
                                     halign='right', valign='middle', color=(0.5,0.5,0.5,1))
                    time_label.bind(width=lambda inst, val: setattr(inst, 'text_size', (val, None)))
                    
                    class_row.add_widget(course_label)
                    class_row.add_widget(time_label)
                    day_section.add_widget(class_row)
                
                schedule_list.add_widget(day_section)