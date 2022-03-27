import pandas as pd

df = pd.read_csv('dirtydata.csv')

# print(df.to_string())
# note that rows 11 and 12 are duplicated
# The duplicated() method returns a Boolean values for each row
# Returns True for every row that is a duplicate, othwerwise False
df.drop_duplicates(inplace=True)
print(df.to_string())

#Notice that row 12 has been removed from the result