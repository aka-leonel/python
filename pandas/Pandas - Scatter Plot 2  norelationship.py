import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot(kind="scatter", x='Duration', y='Maxpulse')

plt.show()
#we can see that there's no relationship between
#esto and aquello