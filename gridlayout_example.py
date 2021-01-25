# Kivy Gridlayout example
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image, AsyncImage
from kivy.core.window import Window

# Set window dimensions
Window.clearcolor = (44/255.0, 62/255.0, 80/255.0, 1)

Window.size = (360, 600)

class GridApp(App):
    def build(self):
        layout = GridLayout(cols=1, row_force_default=True, row_default_height=60, spacing=10, padding=40)
        img = Image(source='ethgas.ico')
        btn1 = Button(text='ETH Gas Station')
        #btn1 = Button(text='ETH Gas Station', size_hint=(None, None), width=200, height=40)
        btn2 = Button(text='ETH Gas Pro')

        btn3 = Button(text='Etherscan Gas')
        btn4 = Button(text='Top 20 Tokens')

        layout.add_widget(img)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout


GridApp().run()
