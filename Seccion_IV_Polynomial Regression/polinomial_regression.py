#Regresión polinómica

#Importamos librerias 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Importamos el dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,-1].values

"""
#Dividimos el dataset en conj de datos para el entrenamiento y datos para testing 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


#Escalado de variables 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""

#Ajuste del modelo de regresion lineal simple

from sklearn.linear_model import LinearRegression
regression_ls = LinearRegression()
regression_ls.fit(X, y)

#Ajuste de la regresion polinomica con el dataset 

from sklearn.preprocessing import PolynomialFeatures
regression_lp = PolynomialFeatures(degree = 4)
X_poly = regression_lp.fit_transform(X)

linear_reg2 = LinearRegression()
linear_reg2.fit(X_poly, y)

#Visualizacion de los resultados del modelo lineal
plt.scatter(X, y, color = "red")
plt.plot(X, regression_ls.predict(X), color = "blue")
plt.title("Modelo de Regresión Lineal")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()

#Visualizacion de los resultados del modelo polinómico

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X_grid, linear_reg2.predict(regression_lp.fit_transform(X_grid)), color = "blue")
plt.title("Modelo de Regresión Polinómica")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()

# Predicción de los modelos
# Sintaxis de doble corchete para hacer la predicción en las últimas versiones de Python (3.7+)
regression_ls.predict([[6.5]])
linear_reg2.predict(regression_lp.fit_transform([[6.5]]))














