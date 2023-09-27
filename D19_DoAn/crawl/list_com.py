from vnstock import stock_historical_data,listing_companies,company_overview,company_profile
import os
import pandas as pd
list_com = listing_companies()['ticker'].sort_values()
print(list_com.keys())
p1 = pd.DataFrame(list_com)
list_info = [(company_profile(str(list_com[i]))["companyProfile"][0]) for i in list_com.keys()]
p1['thong tin'] =  list_info
# print((company_profile(str(list_com[0]))["companyProfile"][0]))
path = ('/').join(os.path.dirname(__file__).split("\\")[:-1])
p1.to_csv(path+"\data\list_com1.csv")
# print(list_com)