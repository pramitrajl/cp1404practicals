""" Dynamic labels program by Pramit"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class MyWidgetsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.country_to_capital = {"Japan": "Tokyo", "Australia": "Canberra", "England": "London"
        }

    def build(self):
        self.title = "Pramit's Widgets"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        for country, capital in self.country_to_capital.items():
            label = Label(text=f"{country}: {capital}")
            self.root.ids.entries_box.add_widget(label)


MyWidgetsApp().run()
