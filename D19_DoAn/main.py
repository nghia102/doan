from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from design.code_helper import code_helper 



class MyApp(MDApp) :
    
    def build(self) :
        screen = Screen()
        self.title ="Predict Project"

        btn_search = MDRectangleFlatButton(text = 'Hello World',
                                  pos_hint = {'center_x': 0.5,'center_y': 0.4},
                                  on_release = self.get_code)
        
        self.code = MDTextField(
                hint_text = "Nhập mã chứng khoán",
                helper_text_mode = "on_focus",
                helper_text = "Nhập mã chứng khoán vào đây",
                pos_hint = {'center_x': 0.5,'center_y': 0.5},
                width = 300,
                size_hint_x = None
                )
        screen.add_widget(btn_search)
        screen.add_widget(self.code)
        return screen
    
    def get_code(self,obj) :
        print(self.code.text)

    
MyApp().run()