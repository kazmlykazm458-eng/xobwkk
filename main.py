from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from core import start_process

class InstaBoostApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(
            text="InstaBoost Pro v1.1",
            font_size='32sp',
            color=(0.6, 0.4, 0.9, 1), # لون بنفسجي
            bold=True
        )
        
        desc = Label(
            text="اضغط على الزر أدناه لزيادة متابعين إنستغرام\n(تأكد من منح صلاحية التخزين)",
            halign='center',
            font_size='18sp'
        )
        
        btn = Button(
            text="ابدأ الرشق الآن",
            size_hint=(None, None),
            size=(250, 60),
            pos_hint={'center_x': 0.5},
            background_color=(0.5, 0, 0.5, 1)
        )
        btn.bind(on_press=self.on_start)
        
        layout.add_widget(title)
        layout.add_widget(desc)
        layout.add_widget(btn)
        
        return layout

    def on_start(self, instance):
        instance.text = "جاري العمل..."
        instance.disabled = True
        start_process()

if __name__ == '__main__':
    InstaBoostApp().run()
