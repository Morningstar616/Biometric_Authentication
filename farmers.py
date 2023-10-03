from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class FarmersAuthenticationScreen(Screen):
    def __init__(self, **kwargs):
        super(FarmersAuthenticationScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20, size_hint=(None, None), size=(400, 300))
        layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        label = Label(text="Farmers Authentication")
        layout.add_widget(label)

        add_fingerprint_button = Button(text="Add Fingerprint", size_hint=(None, None), size=(300, 50))
        add_fingerprint_button.bind(on_press=self.add_fingerprint)
        layout.add_widget(add_fingerprint_button)

        back_button = Button(text="Back", size_hint=(None, None), size=(300, 50))
        back_button.bind(on_press=self.go_to_main_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def add_fingerprint(self, instance):
        print("Adding a fingerprint for Farmers authentication")

    def go_to_main_menu(self, instance):
        sm = self.manager
        sm.current = 'main_menu'
