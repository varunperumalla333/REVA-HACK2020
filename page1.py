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
    MenuScreen:
<MenuScreen>:
    id: scr_io
    name: 'menu'
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
        source: f"output/icon.png"
        size_hint: None, None
        size: "200dp", "200dp"
        pos_hint: {"center_x":.5, "center_y":.7}
    MDFillRoundFlatIconButton:
        text: "start"
        icon:'fire'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.test()
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                title: ''
                id:button
                icon: 'lock'
                type: 'bottom'
                              """
class MenuScreen(Screen):

    def test(self):
        print("screen 1")
class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 0.85
        super().__init__(**kwargs)
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
class AkriaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        screen = Builder.load_string(screen_helper)
        return screen
AkriaApp().run()