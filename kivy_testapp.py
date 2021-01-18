import datetime
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
kivy.require("1.10.1")

# Format current timestamp
date = datetime.datetime.today()
now = date.today()
format = "%a, %b %d %H:%M:%S"
timeStamp = now.strftime(format)

# super() initiates the parent class method as well
class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Trader Gas:"))
        self.traderGas = TextInput(multiline=False)
        self.add_widget(self.traderGas)

        self.add_widget(Label(text="Fast Gas:"))
        self.fastGas = TextInput(multiline=False)
        self.add_widget(self.fastGas)

        self.add_widget(Label(text="Average Gas:"))
        self.avgGas = TextInput(multiline=False)
        self.add_widget(self.avgGas)

        self.add_widget(Label(text="Slow Gas:"))
        self.slowGas = TextInput(multiline=False)
        self.add_widget(self.slowGas)

        self.add_widget(Label(text=timeStamp))
        self.tStamp = TextInput(multiline=False)
        self.add_widget(self.tStamp)




class GasApp(App):
    def build(self):
        return ConnectPage()


if __name__ == "__main__":
    GasApp().run()