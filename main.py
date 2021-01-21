from kivy.app import App
from kivy.clock import Clock
import datetime


# Format current timestamp
date = datetime.datetime.today()
now = date.today()
format = "%a, %b %d %H:%M:%S"
timeStamp = now.strftime(format)


class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.update_label, 1)

    def update_label(self, *args):
        # Update my label
        self.root.ids.counter.text = str(int(self.root.ids.counter.text) + 1)


if __name__ == "__main__":
    MainApp().run()