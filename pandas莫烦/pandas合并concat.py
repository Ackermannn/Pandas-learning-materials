import pandas as pd
import numpy as np

# concartenating

df1 = pd.DataFrame(np.ones(shape=(3,4))*0,
                   columns=['Mon','Tue','Wen','Fir'])
df2 = pd.DataFrame(np.ones(shape=(3,4))*1,
                   columns=['Mon','Tue','Wen','Fir'])
df3 = pd.DataFrame(np.ones(shape=(3,4))*2,
                   columns=['Mon','Tue','Wen','Fir'])

print('df1=',df1,'df2=',df2,'df3=',df3,sep='\n',end='\n\n')

res = pd.concat([df1,df2,df3],axis=0) #axis=0 上下合并
print(res,end='\n\n')
'''
   Mon  Tue  Wen  Fir
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
0  2.0  2.0  2.0  2.0
1  2.0  2.0  2.0  2.0
2  2.0  2.0  2.0  2.0
'''
res1 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res1,end='\n\n')
'''
Mon  Tue  Wen  Fir
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
6  2.0  2.0  2.0  2.0
7  2.0  2.0  2.0  2.0
8  2.0  2.0  2.0  2.0
'''

#join, ['inner','outer']


df1 = pd.DataFrame(np.ones(shape=(3,4))*0,
                   columns=['Mon','Tue','Wen','Sun'],
                   index=[1,2,3])
df2 = pd.DataFrame(np.ones(shape=(3,4))*1,
                   columns=['Mon','Tue','Wen','Fir'],
                   index=[0,2,3])
print('df1=',df1,'df2=',df2,sep='\n',end='\n\n')


res = pd.concat([df1,df2],join='inner',axis=1)
print(res,end='\n\n')

res1 = pd.concat([df1,df2],join_axes=[df1.index],axis=1)
print(res1,end='\n\n')

# df.append()

# https://www.bilibili.com/video/av16378934/?p=16












