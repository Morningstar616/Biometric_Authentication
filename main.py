from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from farmers import FarmersAuthenticationScreen
from admins import AdminsAuthenticationScreen

class MainMenu(Screen):
    pass

class AuthApp(App):
    def build(self):
        sm = ScreenManager()

        main_menu = MainMenu(name='main_menu')

        layout = BoxLayout(orientation='vertical', spacing=20, padding=20, size_hint=(None, None), size=(400, 300))
        layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        Window.clearcolor = get_color_from_hex("#00FF00")

        label = Label(text="Select your authentication type:")
        layout.add_widget(label)

        farmers_button = Button(text="Farmers Authentication", size_hint=(None, None), size=(300, 50))
        admins_button = Button(text="Admins Authentication", size_hint=(None, None), size=(300, 50))

        farmers_button.bind(on_press=self.show_farmers_authentication)
        admins_button.bind(on_press=self.show_admins_authentication)
        layout.add_widget(farmers_button)
        layout.add_widget(admins_button)
        main_menu.add_widget(layout)
        sm.add_widget(main_menu)

        return sm

    def show_farmers_authentication(self, instance):
        sm = self.root
        farmers_authentication_screen = FarmersAuthenticationScreen(name='farmers_auth')
        sm.add_widget(farmers_authentication_screen)
        sm.current = 'farmers_auth'

    def show_admins_authentication(self, instance):
        sm = self.root
        admins_authentication_screen = AdminsAuthenticationScreen(name='admins_auth')
        sm.add_widget(admins_authentication_screen)
        sm.current = 'admins_auth'

if __name__ == '__main__':
    AuthApp().run()
