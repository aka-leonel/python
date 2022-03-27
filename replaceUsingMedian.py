#Calculate the MEDIAN, and replace any empty values with it:
from operator import le
import pandas as pd

lectura = pd.read_csv('data.csv')

mediana = lectura["Calories"].median()

#replace missed values
lectura["Calories"].fillna(mediana, inplace=True)

print(lectura.to_string())
print("La media de calorias es ", mediana)