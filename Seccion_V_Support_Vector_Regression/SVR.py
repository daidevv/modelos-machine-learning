#Support Vector Regression

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# Escalado de variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y.reshape(-1, 1))


# Ajustar la regresión con el dataset
from sklearn.svm import SVR
regression = SVR(kernel = "rbf")
regression.fit(X, y)


# Predicción de nuestros modelos con SVR
y_pred = regression.predict(sc_X.transform(np.array([[6.5]])))
y_pred = sc_y.inverse_transform(y_pred.reshape(-1, 1))


#Reconvertimos los valores de X e y a su estado original
orig_X = sc_X.inverse_transform(X)
orig_y = sc_y.inverse_transform(y)


"""Pruebo y evaluo el rendimiento con R Score
la puntuación R² nos dice qué tan bien se ajusta nuestro modelo a los 
datos al compararlo con la línea promedio de la variable dependiente.
Si la puntuación está más cerca de 1, indica que nuestro modelo funciona
bien, mientras que si la puntuación está más lejos de 1, indica que 
#nuestro modelo no funciona tan bien."""

from sklearn.metrics import r2_score
r2_score(X, y)

"""SALIDA: me da un R Score de 0.6358... logramos una puntuacion de
precision del 63% (comparar r2 score con los modelos de RLS, RLM y RLP)"""

# Visualización de los resultados del modelo con SVR
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X_grid, regression.predict(X_grid), color = "blue")
plt.title("Modelo de Regresión")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()





