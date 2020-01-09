import pandas as pd
import numpy as np
dates = pd.date_range('20190813',periods=6)

df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print('df=')
print(df,'\n')

# df.iloc[2,2] = 111
# df.loc['20190813','B'] = 222
# df[df.A>4] = 0
# df.A[df.A>4] = 0
df['F'] = np.nan
df['E'] = pd.Series([1,3,2,4,5,6],index=pd.date_range('20190813',periods=6))
print(df)

#https://www.bilibili.com/video/av16378934/?p=13
