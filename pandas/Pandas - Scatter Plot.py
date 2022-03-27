#scatter plot needs x and y axis
#in this example we'll use Duration:x
# and Calories:y

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot(kind="scatter", x = 'Duration', y = 'Calories')
plt.show()
#recuerdese que vimos que la relacion entre 
#Duration y calories era de 0.9