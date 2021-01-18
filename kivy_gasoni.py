import datetime
import requests
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
kivy.require("1.10.1")
import defipulse_credentials


# Function to get ETH Gas Station data via the defipulse api
request_data = requests.get(f'https://ethgasstation.info/api/ethgasAPI.json?api-key={defipulse_credentials.defipulseApikey}')
data = request_data.json()

# Create variables in gwei from api data (json)
fast_gwei = data['fast'] / 10
average_gwei = data['average'] / 10
slow_gwei = data['safeLow'] / 10
trader_gwei = data['fastest'] / 10


# Format current timestamp
date = datetime.datetime.today()
now = date.today()
format = "%a, %b %d %H:%M:%S"
timeStamp = now.strftime(format)


# super() initiates the parent class method as well
class GasPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Trader Gas:"))
        self.add_widget(Label(text=str(trader_gwei)))

        self.add_widget(Label(text="Fast Gas:"))
        self.add_widget(Label(text=str(fast_gwei)))

        self.add_widget(Label(text="Average Gas:"))
        self.add_widget(Label(text=str(average_gwei)))

        self.add_widget(Label(text="Slow Gas:"))
        self.add_widget(Label(text=str(slow_gwei)))

        self.add_widget(Label(text="Timestamp"))
        self.add_widget(Label(text=timeStamp))



class GasApp(App):
    def build(self):
        return GasPage()


if __name__ == "__main__":
    GasApp().run()