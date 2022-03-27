#los percentiles dan un numero que indica cuantos valores se hayan debajo de cierto rango
#

import pandas as pd
import numpy as np

full_data = pd.read_csv("data.csv", header=0, sep=",")

Max_Pulse = full_data["Max_Pulse"]
percentile10 = np.percentile(Max_Pulse, 10)
#The 10% percentile of Max_Pulse is 120. This means that 10% of all the training sessions have a Max_Pulse of 120 or lower.


print(percentile10)