from kivy.app import App
from kivy.clock import Clock
import datetime
import requests
import defipulse_credentials


class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.update_label, 1)
        Clock.schedule_interval(self.update_time, 60)
        Clock.schedule_interval(self.update_gas, 60)


    def update_label(self, *args):
        # Update my label
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



if __name__ == "__main__":
    MainApp().run()