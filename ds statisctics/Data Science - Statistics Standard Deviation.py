import pandas as pd
import numpy as np

health_data = pd.read_csv("data.csv", header=0, sep=",")

std = np.std(health_data)

print(std)