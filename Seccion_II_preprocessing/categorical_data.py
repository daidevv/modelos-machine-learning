

#Plantila de pre procesado -- Datos Categóricos

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Importamos el dataset

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#Codificación de datos categóricos

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

xct = ColumnTransformer([("Country", OneHotEncoder(categories = 'auto'), [0])], remainder = 'passthrough')
X = np.array(xct.fit_transform(X))

Transform_y = dataset['Purchased'].replace({'No': 0, 'Yes': 1})
y = Transform_y