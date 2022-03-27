import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Volkswagen"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
#print(myvar)
#print("versión pandas: ", pd.__version__)

#print("Series:\n-------\n")
a = [1,7,2]
myvar2 = pd.Series(a, index = ["x", "y", "z"])
#print(myvar2)

df = pd.read_csv('data.csv')
#print(df.head(3))
#print(df.tail(3))
print(df.info())