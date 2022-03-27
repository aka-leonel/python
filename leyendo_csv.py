import pandas as pd

lectura = pd.read_csv('data.csv')
#leer primeros registros
print(lectura.head())

#leer ultimos registros
#print(lectura.tail())