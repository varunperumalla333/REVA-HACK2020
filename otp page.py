from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.behaviors import CircularRippleBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
working=""
screen_helper = """
ScreenManager:
    id: screen_manager
    ProfileScreen3:
<ProfileScreen3>:
    name: 'profile3'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Akira'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    MDLabel:
        text: 'OTP'
        pos_hint: {'x':0.3,'y':0.09}
    MDTextFieldRect:
        size_hint:.4,.10
        hint_text: "OTP"
        id:my_input
        pos_hint: {'center_x':0.5,'center_y':0.5}
        normal_color: app.theme_cls.accent_color
    MDFillRoundFlatIconButton:
        text: "submit"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press:
  
    MDBottomAppBar:
        MDToolbar:
            title: ''
            id:button
            on_action_button:
            icon: 'home'
            type: 'bottom'
                              """
class ProfileScreen3(Screen):

    def test(self):
        print("screen 1")
class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 0.85
        super().__init__(**kwargs)
sm = ScreenManager()
sm.add_widget(ProfileScreen3(name='profile3'))
class AkriaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        screen = Builder.load_string(screen_helper)
        return screen
AkriaApp().run()
