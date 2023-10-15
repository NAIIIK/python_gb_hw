import pandas as pd
from random import shuffle

lst = ['robot'] * 10
lst += ['human'] * 10
shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data['robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
data['human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)

data = data.drop('whoAmI', axis=1)

print(data.head())
