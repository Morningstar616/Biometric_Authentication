from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

class AdminsAuthenticationScreen(Screen):
    def __init__(self, **kwargs):
        super(AdminsAuthenticationScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20, size_hint=(None, None), size=(400, 300))
        layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        label = Label(text="Admins Authentication")
        layout.add_widget(label)

        add_fingerprint_button = Button(text="Add Fingerprint", size_hint=(None, None), size=(300, 50))
        add_fingerprint_button.bind(on_press=self.add_fingerprint)
        layout.add_widget(add_fingerprint_button)

        back_button = Button(text="Back", size_hint=(None, None), size=(300, 50))
        back_button.bind(on_press=self.go_to_main_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def add_fingerprint(self, instance):
        print("Adding a fingerprint for Admins authentication")
        self.show_notification("Fingerprint added!")

    def go_to_main_menu(self, instance):
        sm = self.manager
        sm.current = 'main_menu'

    def show_notification(self, message, timeout=3):  # You can specify the timeout in seconds
        content = BoxLayout(orientation='vertical', padding=5, spacing=5)
        label = Label(text=message, halign='center', valign='middle')
        content.add_widget(label)

        popup = Popup(title='', content=content, size_hint=(None, None), size=(300, 100),
                      auto_dismiss=False, pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Schedule the popup to close after the specified timeout
        Clock.schedule_once(lambda dt: popup.dismiss(), timeout)

        popup.open()
