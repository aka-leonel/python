#A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
#Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
import pandas as pd

lectura = pd.read_csv('data.csv')
promedio_calorias = lectura["Calories"].mean()
#la magick
lectura["Calories"].fillna(promedio_calorias, inplace=True)

print(lectura.to_string())
print("El promedio fue ", promedio_calorias)