from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.image import Image
import datetime
import requests
import defipulse_credentials

# Set window background color in RGB and Opacity
Window.clearcolor = (74/255.0, 102/255.0, 240/255.0, 1)


class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.update_counter, 1)
        Clock.schedule_interval(self.update_time, 60)
        Clock.schedule_interval(self.update_gas, 60)
        Clock.schedule_interval(self.update_ethspot, 60)


    def update_counter(self, *args):
        self.root.ids.counter.text = str(int(self.root.ids.counter.text) + 1)


    def update_time(self, *args):
        date = datetime.datetime.today()
        now = date.today()
        format = "%a, %b %d %H:%M"
        timeStamp = now.strftime(format)
        self.root.ids.timeLabel.text = str(timeStamp)


    def update_gas(self, *args):
        request_data = requests.get(f'https://ethgasstation.info/api/ethgasAPI.json?api-key={defipulse_credentials.defipulseApikey}')
        data = request_data.json()

        # Create variables in gwei from api data (json)
        fast_gwei = data['fast'] / 10
        average_gwei = data['average'] / 10
        slow_gwei = data['safeLow'] / 10
        trader_gwei = data['fastest'] / 10

        self.root.ids.tradergweiLabel.text = str(trader_gwei)
        self.root.ids.fastgweiLabel.text = str(fast_gwei)
        self.root.ids.avgweiLabel.text = str(average_gwei)
        self.root.ids.slowgweiLabel.text = str(slow_gwei)


    def update_ethspot(self, *args):
        request_price = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
        price = request_price.json()['ethereum']['usd']

        eth_spot = "$" + str(price)

        self.root.ids.ethspotLabel.text = eth_spot



if __name__ == "__main__":
    MainApp().run()