from kivy.app import App
from kivy.uix.image import Image,AsyncImage
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Set window background color in RGB and Opacity
Window.clearcolor = (74/255.0, 102/255.0, 240/255.0, 1)
Window.size = (360, 600)

class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=80)
        btn = Button(text='Gas!', size_hint=(None, None), width=100, height=50, pos_hint={'center_x': 0.5})
        img = Image(source='ethgas.ico')
        layout.add_widget(img)
        layout.add_widget(btn)
        return layout

TestApp().run()