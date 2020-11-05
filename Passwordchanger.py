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
    ProfileScreen8:
<ProfileScreen8>:
    name: 'profile8'
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
        text: 'old password'
        pos_hint: {'x':0.45,'y':0.3}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "password"
        id:my_input
        pos_hint: {'center_x':0.5,'center_y':0.75}
        normal_color: app.theme_cls.accent_color
    MDLabel:
        text: 'new password'
        pos_hint: {'x':0.4,'y':0.15}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "password"
        id:my_input2
        pos_hint: {'center_x':0.5,'center_y':0.6}
        normal_color: app.theme_cls.accent_color
    MDLabel:
        text: 'conform password'
        pos_hint: {'x':0.4,'y':0.0}
    MDTextFieldRect:
        size_hint:.4,.05
        hint_text: "password"
        id:my_input3
        pos_hint: {'center_x':0.5,'center_y':0.45}
        normal_color: app.theme_cls.accent_color
    MDFillRoundFlatIconButton:
        text: "submit"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press:root.bit()
    MDBottomAppBar:
        MDToolbar:
            title: ''
            id:button
            on_action_button: root.manager.current = 'menu'
            icon: 'home'
            type: 'bottom'  """
class ProfileScreen8(Screen):

    def test(self):
        print("screen 1")
class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 0.85
        super().__init__(**kwargs)
sm = ScreenManager()
sm.add_widget(ProfileScreen8(name='profile8'))
class AkriaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        screen = Builder.load_string(screen_helper)
        return screen
AkriaApp().run()
