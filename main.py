from kivy.app import App
from kivy.clock import Clock
import datetime


class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.update_label, 1)
        Clock.schedule_interval(self.update_time, 3)


    def update_label(self, *args):
        # Update my label
        self.root.ids.counter.text = str(int(self.root.ids.counter.text) + 1)


    def update_time(self, *args):
        self.root.ids.timeLabel.text = str(datetime.datetime.now())



if __name__ == "__main__":
    MainApp().run()