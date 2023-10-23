from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList,OneLineListItem
from kivy.lang import Builder
from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.uix.scrollview import ScrollView
import matplotlib
matplotlib.use("module://kivy.garden.matplotlib.backend_kivy")
from chart.chart import candleStick
from design.code_helper import code_helper 
import pandas as pd
import os
#read csv
import pandas as pd
import os 
#plot chart
import plotly.graph_objects as go
import plotly.express as px
#matplotlib 
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates

class MyApp(MDApp) :
    
    def build(self) :

        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
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
            scroll = ScrollView()
            # scroll.add_widget(FigureCanvasKivyAgg(candleStick()))
            screen.add_widget(FigureCanvasKivyAgg(candleStick()))
            Builder.load_file('matty.kv')
            # screen.add_widget(info)
def get_data() :
    path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
    data_result = pd.read_csv(path+'/d19_doan/data/data.csv')


    # data_result = data_result.set_index('Date')
    # data_result.drop('Unnamed: 0',axis = 1,inplace = True)
    data_result['Difference'] = [data_result['Close'][i]-data_result['Open'][i] for i in range(len(data_result))]
    data_result = data_result.dropna()
    return data_result

import plotly.graph_objects as go
import plotly.express as px


def candleStick() :
    data_result = get_data()
    ohlc = data_result.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
    # Converting date into datetime format
    ohlc['Date'] = pd.to_datetime(ohlc['Date'])
    ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
    ohlc = ohlc.astype(float)
    # Creating Subplots
    fig, ax = plt.subplots()
    candlestick_ohlc(ax, ohlc.values, width=0.6,
                    colorup='green', colordown='red', alpha=0.8)
    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    fig.suptitle('Daily Candlestick Chart of NIFTY50')
    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    fig.tight_layout()
    
    
    def press(event):
        print('press released from test', event.x, event.y, event.button)


    def release(event):
        print('release released from test', event.x, event.y, event.button)


    def keypress(event):
        print('key down', event.key)


    def keyup(event):
        print('key up', event.key)


    def motionnotify(event):
        print('mouse move to ', event.x, event.y)


    def resize(event):
        print('resize from mpl ', event)


    def scroll(event):
        print('scroll event from mpl ', event.x, event.y, event.step)


    def figure_enter(event):
        print('figure enter mpl')


    def figure_leave(event):
        print('figure leaving mpl')


    def close(event):
        print('closing figure')


    fig.canvas.mpl_connect('button_press_event', press)
    fig.canvas.mpl_connect('button_release_event', release)
    fig.canvas.mpl_connect('key_press_event', keypress)
    fig.canvas.mpl_connect('key_release_event', keyup)
    fig.canvas.mpl_connect('motion_notify_event', motionnotify)
    fig.canvas.mpl_connect('resize_event', resize)
    fig.canvas.mpl_connect('scroll_event', scroll)
    fig.canvas.mpl_connect('figure_enter_event', figure_enter)
    fig.canvas.mpl_connect('figure_leave_event', figure_leave)
    fig.canvas.mpl_connect('close_event', close)
    return plt.gcf()            

    
MyApp().run()