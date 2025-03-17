# Regresión lineal simple

#Importamos las librerias 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Importamos el dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

#Dividimos el dataset en conj de datos para el entrenamiento y datos para testing 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

#Escalado de variables - no necesario en el modelo de RLS
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""

#Creación del modelo de regresión lineal simple - Fase de entrenamiento
from sklearn.linear_model import LinearRegression 
regression = LinearRegression() 
regression.fit(X_train, y_train)  

#Predecimos el conjunto de test (Creamos un vector de predicciones)
y_pred = regression.predict(X_test) 


#Visualización de los resultados de entrenamiento...
plt.scatter(X_train, y_train, color = "red") 
plt.plot(X_train, regression.predict(X_train), color ="blue"
plt.title("Sueldos vs.Años de experiencia(conjunto de entrenamiento)")
plt.show()


#Visualización de los resultados de testing
plt.scatter(X_test, y_test, color = "red") 
plt.plot(X_train, regression.predict(X_train), color ="blue")   
plt.title("Sueldos vs.AÃ±os de experiencia(conjunto de testing)")
plt.show()










