import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require("1.10.1")

class GasApp(App):
    def build(self):
        return Label(text="Hello!")


if __name__ == "__main__":
    GasApp().run()