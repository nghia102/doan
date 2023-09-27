#read csv
import pandas as pd
import os 
#plot chart
import plotly.graph_objects as go
import plotly.express as px
# lay path
path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
data_result = pd.read_csv(path+'/data/data.csv')


data_result = data_result.set_index('Date')
data_result.drop('Unnamed: 0',axis = 1,inplace = True)
data_result['Difference'] = [data_result['Close'][i]-data_result['Open'][i] for i in range(len(data_result))]
data_result = data_result.dropna()


print(data_result)

import plotly.graph_objects as go
import plotly.express as px
def candleStick() :
    fig1 = go.Figure(go.Candlestick(x = data_result.index,
                                    open = data_result['Open'],
                                    close = data_result['Close'],
                                    high = data_result['High'],
                                    low = data_result['Low']))
    fig1.show()
def lineChart() :
    fig = px.line(data_result, x=data_result.index, y="Close", title='Close data')
    fig.show()



candleStick()
lineChart()