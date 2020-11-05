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
    ProfileScreen2:
<ProfileScreen2>:
    name: 'profile2'
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
        source: f"output/ip5.png"
        size_hint: None, None
        size: "600dp", "300dp"
        pos_hint: {"center_x": .5, "center_y": .5} 
    MDLabel:
        text: 'please avoid too much lighting in back ground'
        halign: "center"
        pos_hint: {'x':-0.0,'y':-.33}  
    MDFillRoundFlatIconButton:
        text: "SCAN"
        icon:''
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:  """
class ProfileScreen2(Screen):

    def test(self):
        print("screen 1")
class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 0.85
        super().__init__(**kwargs)
sm = ScreenManager()
sm.add_widget(ProfileScreen2(name='profile2'))
class AkriaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        screen = Builder.load_string(screen_helper)
        return screen
AkriaApp().run()