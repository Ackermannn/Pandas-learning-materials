"""
Python：DataFrame转dict字典
https://www.cnblogs.com/xiaolan-Lin/p/12091629.html
"""

import pandas as pd

item = pd.DataFrame({'item_name': ["a", "b", "c"],
                     'item_num': [87974, 975646, 87974]},
                    index=[0, 1, 2])
print(item)

# item_name 作为键值， item_num作为value
item_dict = item.set_index('item_name')['item_num'].to_dict()
print(item_dict)