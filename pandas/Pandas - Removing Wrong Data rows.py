import pandas as pd

df = pd.read_csv('dirtydata.csv')


#wrong data: you got two ways
#replace it or remove it
#here we remove

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)

print(df.to_string())