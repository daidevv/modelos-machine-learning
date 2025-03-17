#Script completo de toda la fase de preprocesamiento

#Importamos librerias 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Importamos el dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#Tratamiento de los valores NaN usando Sklearn
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
Imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])

# Codificamos (tranformamos) los datos categóricos a numéricos
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
xct = ColumnTransformer([("Country", OneHotEncoder(categories = 'auto'), [0])], remainder = 'passthrough')
X = np.array(xct.fit_transform(X))


Transform_y = dataset['Purchased'].replace({'No': 0, 'Yes': 1})
y = Transform_y

#División del dataset en conj. de datos para fase de entrenamiento y fase de test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


#Escalado de valores numéricos
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)























