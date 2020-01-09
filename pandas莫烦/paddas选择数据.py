import pandas as pd
import numpy as np
dates = pd.date_range('20190813',periods=6)

df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print('df=')
print(df,'\n')

print('>>>df[\'A\']')
print(df['A'],'\n')

print('>>>df.A')
print(df.A,'\n')

print('>>>df[0:3]')
print(df[0:3],'\n')

print('>>>df[\'20190813\':\'20190815\']')
print(df['20190813':'20190815'],'\n')

#select by label: loc

print('>>>df.loc[\'20190814\']')
print(df.loc['20190814'],'\n')

print(">>>df.loc[:,['A','B']]")
print(df.loc[:,['A','B']],'\n')

print(">>>df.loc['20190813',['A','B']]")
print(df.loc['20190813',['A','B']],'\n')

#selet by position: iloc
print(df.iloc[[0,1,3],1:3])

#mixed selection :ix
print(df.ix[3,['A','C']])  #要被弃用

#Boolean indexing
print(df[df.A>8])
