#Calculate the MODE, and replace any empty values with it:
import pandas as pd

#read the file
lectura = pd.read_csv("data.csv")

#depeche mode
moda = lectura["Calories"].mode()[0]

#replace missed values
lectura["Calories"].fillna(moda, inplace=True)

print(lectura.to_string())
print("La moda de calorias es ", moda)