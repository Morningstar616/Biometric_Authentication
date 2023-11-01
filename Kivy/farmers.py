from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock

class FarmersAuthenticationScreen(Screen):
    def __init__(self, **kwargs):
        super(FarmersAuthenticationScreen, self).__init__(**kwargs)

        layout = MDBoxLayout(orientation='vertical', padding=40, spacing=20)

        label = MDLabel(text="Farmers Authentication", theme_text_color="Primary", halign='center', font_style="H4")
        layout.add_widget(label)

        add_fingerprint_button = MDRaisedButton(text="Add Fingerprint", size_hint=(None, None), size=(250, 40), halign='center')
        add_fingerprint_button.pos_hint = {'center_x': 0.5} 
        add_fingerprint_button.bind(on_release=self.add_fingerprint)
        layout.add_widget(add_fingerprint_button)

        back_button = MDRaisedButton(text="Back to Main Menu", size_hint=(None, None), size=(200, 40))
        back_button.pos_hint = {'right': 1}
        back_button.bind(on_release=self.go_to_main_menu)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def add_fingerprint(self, instance):
        print("Adding a fingerprint for Farmers authentication")
        self.show_notification("Fingerprint added")

    def go_to_main_menu(self, instance):
        sm = self.manager
        sm.current = 'main_menu'
    
    def show_notification(self, message, timeout=3):  # You can specify the timeout in seconds
        notification_content = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        label = MDLabel(
            text=message,
            halign='center',
            valign='middle',
            font_style="Body1"
        )
        notification_content.add_widget(label)

        dialog = MDDialog(
            title='',
            type="custom",
            content_cls=notification_content,
            size_hint=(None, None),
            size=(300, 150)
        )
        dialog.open()

        # Schedule the dialog to close after the specified timeout
        Clock.schedule_once(lambda dt: dialog.dismiss(), timeout)
