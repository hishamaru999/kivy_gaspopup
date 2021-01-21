from kivy.app import App
from kivy.clock import Clock
import datetime


class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.update_label, 1)

    def get_time(self):
        # Format current timestamp
        date = datetime.datetime.today()
        now = date.today()
        format = "%a, %b %d %H:%M:%S"
        timeStamp = now.strftime(format)

    def update_label(self, *args):
        # Update my label
        self.root.ids.counter.text = str(int(self.root.ids.counter.text) + 1)
        self.root.ids.timeLabel.text = "new time"


if __name__ == "__main__":
    MainApp().run()