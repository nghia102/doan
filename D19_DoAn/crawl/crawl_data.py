<<<<<<< HEAD
# #Thu vien gui request trang web va lay response
# import requests
# #Thu vien phan tich cac bang trong web HTML
# #pip install html-table-parser-python3
# from html_table_parser.parser import HTMLTableParser

# # Su dung dataframe
import pandas as pd
# import datetime as dt
# import numpy as np
# #import DataFrame as df

# from sklearn.preprocessing import MinMaxScaler # chuan hoa du lieu
# from sklearn.metrics import r2_score # do muc do phu hop
# from sklearn.metrics import mean_absolute_error # do sai so tuyet doi trung binh
# from sklearn.metrics import mean_absolute_percentage_error # do % sai so tuyet doi trung binh

# from keras.callbacks import ModelCheckpoint # luu huan luyen tot nhat
# from keras.models import Sequential # dau vao du lieu cho model
# from keras.layers import LSTM # hoc phu thuoc
# from keras.layers import Dropout # tranh hoc tu
# from keras.layers import Dense # Dau ra
# import tensorflow as tf
# from tensorflow import keras #load mohinh
# import requests

from vnstock import stock_historical_data,listing_companies
import datetime
import os


#crawl data
time = datetime.date.today()

list_com = listing_companies()['ticker']
def crawl(ticker_stock) :
<<<<<<< HEAD
    data_result = stock_historical_data(ticker_stock, "2010-01-01", str(time), "1D")
    print(data_result.columns)


    #doi ten cot
    data_result.rename(columns = {'time':'Date','close':'Close','volume':'Volume','open':'Open','high':'High','low':'Low'},inplace=True) 
    #data_result = pd.Series(data_result.values.flatten())
    #print(data_result)
    #chuan hoa kieu du lieu
    # data_result['Index'] = pd.to_numeric(data_result['Index'].astype(str).str.replace('#','').astype(int))
    # data_result['Date'] = pd.to_datetime(data_result['Date'].astype(str).str.strip(), format='%Y-%m-%d').to_string()
    # data_result['Difference'] = pd.to_numeric(data_result['Difference'].astype(str).str.replace('%','').astype(float))
    data_result['Close'] = data_result['Close'].astype(float)
    data_result['Volume'] = pd.to_numeric(data_result['Volume'].astype(str).str.replace(',','').astype(int))
    data_result['Open'] = data_result['Open'].astype(float)
    data_result['High'] = data_result['High'].astype(float)
    data_result['Low'] = data_result['Low'].astype(float)
    print(data_result)
    print(data_result.info())

    path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
    data_result.to_csv(path+"\data\data_json\data"+ticker_stock+".csv")

    path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
    data_result = pd.read_csv(path+"\data\data_json\data"+ticker_stock+".csv")

    data_result = data_result.set_index('Date')
    data_result.drop('Unnamed: 0',axis = 1,inplace = True)
    data_result['Difference'] = [data_result['Close'][i]-data_result['Open'][i] for i in range(len(data_result))]
    data_result = data_result.dropna()

    path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
    data_result.to_json(path+"\data\data_json\data"+ticker_stock+".json")

crawl("QBS")
=======
    # ticker_stock = "AAM"
    try :
        data_result = stock_historical_data(ticker_stock, "2010-01-01", str(time), "1D")
    
        print(data_result.columns)


        #doi ten cot
        data_result.rename(columns = {'time':'Date','close':'Close','volume':'Volume','open':'Open','high':'High','low':'Low'},inplace=True) 
        #data_result = pd.Series(data_result.values.flatten())
        #print(data_result)
        #chuan hoa kieu du lieu
        # data_result['Index'] = pd.to_numeric(data_result['Index'].astype(str).str.replace('#','').astype(int))
        data_result['Date'] = (data_result['Date'].astype(str).str.strip())
        # data_result['Difference'] = pd.to_numeric(data_result['Difference'].astype(str).str.replace('%','').astype(float))
        data_result['Close'] = data_result['Close'].astype(float)
        data_result['Volume'] = pd.to_numeric(data_result['Volume'].astype(str).str.replace(',','').astype(int))
        data_result['Open'] = data_result['Open'].astype(float)
        data_result['High'] = data_result['High'].astype(float)
        data_result['Low'] = data_result['Low'].astype(float)
        # data_result['index_column'] = data_result.index

        # path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
        # data_result.to_csv(path+"\data\data_gia\data_"+ticker_stock+".csv")

        # path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
        # data_result = pd.read_csv(path+"\data\data_gia\data_"+ticker_stock+".csv")

        # data_result = data_result.reset_index().set_index('Date')
        
        # data_result.drop('Unnamed: 0',axis = 1,inplace = True)
        print(data_result)
        print(data_result.info())
        # data_result = data_result.set_index("Date")
        data_result['Difference'] = [data_result['Close'][i]-data_result['Open'][i] for i in range(len(data_result))]
        data_result = data_result.dropna()
        # data_result.reset_index(inplace=True)
        path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
        data_result.to_json(path+"\data\data_gia\data_"+ticker_stock+".json",orient="records")
    except UnboundLocalError : 
        pass

# data_result.to_csv(path+"\data\data_"+ticker_stock+".csv")
# print(type(list_com[1]))
for i in range(250,len(list_com)) :
    crawl(list_com[i])

>>>>>>> 0258eb8a90cb3f97048d8b7b340d1fe211adccdc
=======
# #Thu vien gui request trang web va lay response
# import requests
# #Thu vien phan tich cac bang trong web HTML
# #pip install html-table-parser-python3
# from html_table_parser.parser import HTMLTableParser

# # Su dung dataframe
import pandas as pd
# import datetime as dt
# import numpy as np
# #import DataFrame as df

# from sklearn.preprocessing import MinMaxScaler # chuan hoa du lieu
# from sklearn.metrics import r2_score # do muc do phu hop
# from sklearn.metrics import mean_absolute_error # do sai so tuyet doi trung binh
# from sklearn.metrics import mean_absolute_percentage_error # do % sai so tuyet doi trung binh

# from keras.callbacks import ModelCheckpoint # luu huan luyen tot nhat
# from keras.models import Sequential # dau vao du lieu cho model
# from keras.layers import LSTM # hoc phu thuoc
# from keras.layers import Dropout # tranh hoc tu
# from keras.layers import Dense # Dau ra
# import tensorflow as tf
# from tensorflow import keras #load mohinh
# import requests

from vnstock import stock_historical_data,listing_companies
import datetime
import os


#crawl data
time = datetime.date.today()

list_com = listing_companies()['ticker']
def crawl(ticker_stock) :
    # ticker_stock = "AAM"
    try :
        data_result = stock_historical_data(ticker_stock, "2010-01-01", str(time), "1D")
    
        print(data_result.columns)


        #doi ten cot
        data_result.rename(columns = {'time':'Date','close':'Close','volume':'Volume','open':'Open','high':'High','low':'Low'},inplace=True) 
        #data_result = pd.Series(data_result.values.flatten())
        #print(data_result)
        #chuan hoa kieu du lieu
        # data_result['Index'] = pd.to_numeric(data_result['Index'].astype(str).str.replace('#','').astype(int))
        data_result['Date'] = (data_result['Date'].astype(str).str.strip())
        # data_result['Difference'] = pd.to_numeric(data_result['Difference'].astype(str).str.replace('%','').astype(float))
        data_result['Close'] = data_result['Close'].astype(float)
        data_result['Volume'] = pd.to_numeric(data_result['Volume'].astype(str).str.replace(',','').astype(int))
        data_result['Open'] = data_result['Open'].astype(float)
        data_result['High'] = data_result['High'].astype(float)
        data_result['Low'] = data_result['Low'].astype(float)
        # data_result['index_column'] = data_result.index

        # path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
        # data_result.to_csv(path+"\data\data_gia\data_"+ticker_stock+".csv")

        # path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
        # data_result = pd.read_csv(path+"\data\data_gia\data_"+ticker_stock+".csv")

        # data_result = data_result.reset_index().set_index('Date')
        
        # data_result.drop('Unnamed: 0',axis = 1,inplace = True)
        print(data_result)
        print(data_result.info())
        # data_result = data_result.set_index("Date")
        data_result['Difference'] = [data_result['Close'][i]-data_result['Open'][i] for i in range(len(data_result))]
        data_result = data_result.dropna()
        # data_result.reset_index(inplace=True)
        path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
        data_result.to_json(path+"\data\data_gia1\data_"+ticker_stock+".json",orient="records")
    except UnboundLocalError : 
        pass

# data_result.to_csv(path+"\data\data_"+ticker_stock+".csv")
# print(type(list_com[1]))
for i in range(250,len(list_com)) :
    crawl(list_com[i])

>>>>>>> 8c508b64162773fb670a3ebb6f059e91d8ee7c5f
