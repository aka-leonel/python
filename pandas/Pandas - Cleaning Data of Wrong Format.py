#lines 22 and 26 in 'data.csv' are not a valid dates 
#row 22 has  NaN  (NaN)
#row 26 20201226  (int)

import pandas as pd

lectura = pd.read_csv('dirtydata.csv')

lectura['Date'] = pd.to_datetime(lectura['Date'])

print(lectura.to_string())
#aun queda por una fila con valor NaT 
#vamos a removerla

lectura.dropna(subset=['Date'], inplace=True)
print(lectura.to_string())
#notese que ya no esta la fila 22