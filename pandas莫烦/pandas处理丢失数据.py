import pandas as pd
import numpy as np
dates = pd.date_range('20190813',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print('df=')
print(df,'\n')

#print(df.dropna(axis = 0,how = 'any'))
    # how={'any','all'} 丢掉数据  all:全为nan才丢掉

print(df.fillna(value=0)) #填充

print(df.isnull())#判断

print(np.any(df.isnull()) == True)
