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
# lay path
def get_data() :
    path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
    data_result = pd.read_csv(path+'/data/data.csv')


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
    
    return plt.gcf()


def lineChart() :
    data_result = get_data()
    fig = px.line(data_result, x=data_result.index, y="Close", title='Close data')
    fig.show()



# candleStick()
# lineChart()