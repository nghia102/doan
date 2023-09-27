from sklearn.preprocessing import MinMaxScaler # chuan hoa du lieu


sc = MinMaxScaler(feature_range(0,1))
sc_train =sc.fit_transform(data.reshape(-1,1))
print(type(sc_train))
for i in range(3) :
    # print(sc_train)
    dudoan = []

    dudoan.append(sc_train[len(sc_train)-50:len(sc_train),0])

    dudoan = np.array(dudoan)
    dudoan = np.reshape(dudoan,(dudoan.shape[0],dudoan.shape[1],1))

    result = final_model.predict(dudoan)   
    print(result)
result = sc.inverse_transform(result)/1000
print(f"thuc : {data[len(data)-1]} du doan tiep theo : {result}")
print(f"do lech chuan theo VND {mean_absolute_error(df_test['Close'],df_test['predict'])/1000}")
print(f"do lech chuan tuyet doi {mean_absolute_percentage_error(df_test['Close'],df_test['predict'])}")