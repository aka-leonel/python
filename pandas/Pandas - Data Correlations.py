#esto es mucho muy importante
#corr() returns values [-1, 1]
#1/-1 are perfect relationships (lineal or lineal^-1)

import pandas as pd

df = pd.read_csv('data.csv')

print(df.corr())