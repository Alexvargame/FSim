from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.list import OneLineAvatarIconListItem

KV = '''
Screen:
    
    ScreenManager:                      
        Screen:                
            id: main_screen    
            name: 'main_window'
            

<ItemDialog>:
    id: item_dialog
    text: "One-line item with avatar"
    on_size:
        self.ids._right_container.width = container.width
        self.ids._right_container.x = container.width

    IconLeftWidget:
        icon: "cog"

    YourContainer:
        id: container

        MDTextField
            id: f_field
            hint_text: "minus"

'''

class ItemDialog(OneLineAvatarIconListItem):
    def __init__(self, cont):
        super(ItemDialog, self).__init__()
        print(self.ids)
        self.cont = cont
        self.ids.f_field.hint_text=cont

class YourContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True

    #.add_widget(MDTextField)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        print(self.screen.ids)
        cont = [1,2,3,4,5,6,7]
        box = BoxLayout(orientation='vertical')
        self.screen.add_widget(box)
        for c in cont:
            box.add_widget(ItemDialog(str(c)))

    def build(self):
        self.theme_cls.theme_style = "Light"
        return self.screen


MainApp().run()