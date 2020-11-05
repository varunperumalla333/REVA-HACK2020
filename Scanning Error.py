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
    ProfileScreen4:
<ProfileScreen4>:
    name: 'profile4'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Akira'
            elevation:5
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    
    CircularRippleButton:
        source: f"output/sad3.png"
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
    MDLabel:
        text: 'ERROR'
        theme_text_color: "Error"
        halign: "center"
        pos_hint: {'x':0.0,'y':-.3}
    MDLabel:
        text: 'Please show your face to camera'
        halign: "center"
        pos_hint: {'x':-0.0,'y':-.33}
      
    MDFillRoundFlatIconButton:
        text: "scan again"
        icon:'home'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:root.manager.current = 'profile2'  """
class ProfileScreen4(Screen):

    def test(self):
        print("screen 1")
class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 0.85
        super().__init__(**kwargs)
sm = ScreenManager()
sm.add_widget(ProfileScreen4(name='profile4'))
class AkriaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        screen = Builder.load_string(screen_helper)
        return screen
AkriaApp().run()
