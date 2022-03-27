from statistics import median, multimode
import numpy as np
from statistics import multimode

#listado
values = [4, 12, 7, 14, 12]

#calculos
media = np.mean(values)
mediana = np.median(values)
moda = multimode(values)
desvioEstandar = np.std(values)

print(values)
print("media: ", media)
print("mediana: ", mediana)
print("moda: ", moda)
print("desvio estandar: ", desvioEstandar)