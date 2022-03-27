#Use the 'kind' argument to specify that you want a histogram
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot(kind="hist", y="Duration", x="Calories")
#df["Duration"].plot(kind="hist")
plt.show()