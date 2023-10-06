from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.garden.matplotlib import FigureCanvasKivyAgg

from chart.chart import candleStick
from design.code_helper import code_helper 
import pandas as pd
import os

class MyApp(MDApp) :
    
    def build(self) :
        screen = Screen()
        self.title ="Predict Project"
        self.code = MDTextField(
                        hint_text = "Nhập mã chứng khoán",
                        helper_text_mode = "on_focus",
                        helper_text = "Nhập mã chứng khoán vào đây",
                        pos_hint = {'center_x': 0.5,'center_y': 0.5},
                        width = 300,
                        size_hint_x = None
                        )
        
        btn_search = MDRectangleFlatButton(text = 'Tìm kiếm',
                                  pos_hint = {'center_x': 0.5,'center_y': 0.4},
                                  on_press = lambda x :self.get_code(screen=screen,code = self.code.text)
                                  )
        
        
        screen.add_widget(btn_search)
        screen.add_widget(self.code)
        return screen 
    
    def get_code(self,screen,code) :
        code = str(code).upper()
        path = ('/').join(os.path.dirname(__file__).split("\\"))
        list_com = pd.read_csv(path+'/data/list_com1.csv')
        list_com = pd.concat([list_com['ticker'],list_com['thong tin']],axis=1)
        list_com = pd.DataFrame(list_com).set_index("ticker")
        if code not in list_com.index :
            dialog = MDDialog(title = "Lỗi",text = "Không tìm được mã")
            dialog.open()
        else :
            dialog = MDDialog(title = "Success",text = "Tìm thấy mã rồi nè")
            dialog.open()
            print(list_com)
            info = MDLabel(text = str(list_com.at[code,"thong tin"]))
            screen.clear_widgets()
            screen.add_widget(FigureCanvasKivyAgg(candleStick()))
            # screen.add_widget(info)


        
            

    
MyApp().run()