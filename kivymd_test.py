# kivymd test
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton


class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        # label = MDLabel(text='Hello World!', halign='center', theme_text_color='Error')
        # label2 = MDLabel(text='How Now', halign='center', theme_text_color='Custom',
        # text_color = (51 / 255.0, 0 / 255.0, 102 / 255.0, 1), font_style = 'H4')
        # iconLabel = MDIcon(icon='gas-station', halign='center')

        btnFlat = MDFlatButton(text='No No!', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btnFlat)

        return screen


DemoApp().run()
