import os 
import pandas as pd
import datetime as dt
import numpy as np

from sklearn.preprocessing import MinMaxScaler # chuan hoa du lieu
from sklearn.metrics import r2_score # do muc do phu hop
from sklearn.metrics import mean_absolute_error # do sai so tuyet doi trung binh
from sklearn.metrics import mean_absolute_percentage_error,mean_squared_error

from tensorflow import keras #load mohinh

import plotly.graph_objects as go
import plotly.express as px

path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
data_result = pd.read_csv(path+'/data/data.csv')
data_result = data_result.set_index('Date')
data = data_result['Close']
data1 = data
data = data.values.reshape(-1,1)
train_data = data[:len(data)//2]
sc = MinMaxScaler(feature_range=(0,1))
sc_train =sc.fit_transform(data.reshape(-1,1))


#loadmodel
final_model = keras.models.load_model('save_model.hdf5')

length = len(data)//2
test_data = data[length:]
x_test, y_test = [] , []
for i in range(len(test_data)) :
    x_test.append(sc_train[length-50+i:length+i,0])
    y_test.append(sc_train[length+i])

x_test = np.array(x_test)
y_test = np.array(y_test)
x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
# y_test = np.reshape(y_test,(y_test.shape[0],1))

test_model = final_model.predict(x_test)
test_model = sc.inverse_transform(test_model)
#print(test_model)
for i in range(3) :
    # print(sc_train)
    dudoan = []

    dudoan.append(sc_train[len(sc_train)-50:len(sc_train),0])

    dudoan = np.array(dudoan)
    dudoan = np.reshape(dudoan,(dudoan.shape[0],dudoan.shape[1],1))

    result = final_model.predict(dudoan)   
    print(result)
result = sc.inverse_transform(result)
df_test = pd.DataFrame(data1[length:])
#print(df_test)
df_test['predict'] = test_model
# print(df_test)
fig = px.line(df_test, x=df_test.index, y=["Close","predict"], title='Close data')
# print(len(test_model),len(test_data))

# print(test_model , test_data)

print("Giá hiện tại: ", test_model[len(test_model)-1])

print("Giá dự đoán sau 3 ngày nữa: ", result)

print("RMSE: ",mean_squared_error(test_data,test_model,squared= False))

print("Độ lệch chuẩn theo VND: ", mean_absolute_error(df_test['Close'],df_test['predict']))

print("Độ lệch chuẩn tuyệt đối theo phần trăm: ", mean_absolute_percentage_error(df_test['Close'],df_test['predict'])*100)

# fig.show()