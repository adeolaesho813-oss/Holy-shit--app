from kivy.app import App
from kivy.uix.label import Label

class HolyShitApp(App):
    def build(self):
        return Label(text="Holy Shit App Working!")

HolyShitApp().run()
