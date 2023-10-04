# main.py
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.widget import Widget
from farmers import FarmersAuthenticationScreen  
from admins import AdminsAuthenticationScreen

Builder.load_string('''
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        spacing: '20dp'
        padding: '20dp'
        size_hint: None, None
        size: '400dp', '300dp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        
        MDLabel:
            text: "Select your authentication type:"
            theme_text_color: "Secondary"
            halign: 'center'
        
        MDRaisedButton:
            text: 'Farmers Authentication'
            size_hint: None, None
            size: '300dp', '50dp'
            pos_hint: {'center_x': 0.5}
            on_release: root.show_farmers_authentication()
        
        MDRaisedButton:
            text: 'Admins Authentication'
            size_hint: None, None
            size: '300dp', '50dp'
            pos_hint: {'center_x': 0.5}
            on_release: root.show_admins_authentication()
''')

class MenuScreen(Screen):
    def show_farmers_authentication(self):
        self.manager.current = 'farmers_auth'

    def show_admins_authentication(self):
        self.manager.current = 'admins_auth'

class AuthApp(MDApp):
    def build(self):
        Window.clearcolor = get_color_from_hex("#00FF00")
        sm = ScreenManager()

        main_menu = MenuScreen(name='main_menu')
        sm.add_widget(main_menu)

        farmers_authentication_screen = FarmersAuthenticationScreen(name='farmers_auth')
        sm.add_widget(farmers_authentication_screen)

        
        admins_authentication_screen = AdminsAuthenticationScreen(name='admins_auth')
        sm.add_widget(admins_authentication_screen)

        return sm


if __name__ == '__main__':
    AuthApp().run()

