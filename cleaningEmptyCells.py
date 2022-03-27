# asegurese de parase estar en el mismo
# path que el archivo data.csv

import pandas as pd

lectura = pd.read_csv('data.csv')

# por defecto se muestran head(5) y tail(5)
# print(lectura)

# y si quiero mostrar todos los registros?
# print(lectura.to_string())

# esta lectura no retornara las celdas vacias
#lecturaLimpia = lectura.dropna()

# print first/last 3 rows
# print(lectura.head(3))
# print(lectura.tail(3))

# prints summary info: nº col/raws, null values, etc
# print(lectura.info())


# --------Data cleaning block------------
# deleting empty rows
#lecturaLimpia = lectura.dropna()
# print(lecturaLimpia.to_string())

# Replace Empty Values
#lectura.fillna(130, inplace=True)
#print(lectura.to_string())

#Replace Only For Specified Columns
#lectura["Calories"].fillna(130, inplace=True)

