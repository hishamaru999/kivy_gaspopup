from kivy.app import App
from kivy.uix.image import Image,AsyncImage
from kivy.core.window import Window

# Set window background color in RGB and Opacity
Window.clearcolor = (74/255.0, 102/255.0, 240/255.0, 1)

class TestApp(App):
    def build(self):
        img = AsyncImage(source='https://ethgasstation.info/images/ETHGasStation.png')
        return img

TestApp().run()