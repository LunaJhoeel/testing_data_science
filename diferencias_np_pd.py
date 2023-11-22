import pandas as pd
import numpy as np

# Ejemplo de datos
data = np.array([1, 2, 3, 4, 5])

# Calculando la desviación estándar con NumPy
std_numpy = np.std(data)

# Calculando la desviación estándar con Pandas 
serie_pandas = pd.Series(data)
std_pandas = serie_pandas.std(ddof=0) # con ddof=0 (Correcion de Bessel)

print("Desviación estándar en NumPy:", std_numpy)
print("Desviación estándar en Pandas", std_pandas)
