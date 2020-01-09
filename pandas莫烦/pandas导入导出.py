import numpy as np
import pandas as pd

data = pd.read_csv('Student.csv')
print(data)

data.to_pickle('Student.pickle')
