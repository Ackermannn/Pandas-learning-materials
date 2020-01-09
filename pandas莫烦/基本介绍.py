import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])
'''
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
'''
dates = pd.date_range('20190812',periods=6)
'''
DatetimeIndex(['2019-08-12', '2019-08-13', '2019-08-14', '2019-08-15',
               '2019-08-16', '2019-08-17'],
              dtype='datetime64[ns]', freq='D')
'''
df = pd.DataFrame(np.random.randn(6,4),index = dates,columns=['a','b','c','d'])
print('df =')
print(df)

df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print('df1 =')
print(df1)

df2 = pd.DataFrame({'A':1,'B':['first','second']})  # 字典形式
print('df2 =')
print(df2)
print('df2.dtypes =')
print(df2.dtypes)
print('df2.index =')
print(df2.index)
print('df2.columns =')
print(df2.columns)
# df2.describe()
# df2.T
# df2.sort_index(axis=1,ascending=False) 排序
# df2.sort_values(by='A') #对单行数据排序
