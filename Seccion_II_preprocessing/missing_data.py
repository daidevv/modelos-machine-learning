
#Plantilla de pre procesado -- Datos faltantes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Importamos el dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#Tratamiento de los valores NaN
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
Imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])
