#"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

import pandas as pd

#df stands for dataFrame (file reading returns a bidimiensional array)
df = pd.read_csv('dirtydata.csv')
#row 7 has a wrong value, 450 instead 45
#print(df.to_string())

#For small data sets you might be able to replace the wrong data one by one, but not for big data sets.

#To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

print(df.to_string())
#se puede ver fila[7][duration] con valor 120

