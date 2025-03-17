# MODELOS DE MACHINE LEARNING
<p align="left">
El repositorio contiene una serie de modelos de Machine Learning. Antes de entrenar a los modelos se llevó a cabo un preprocesamiento de los datos para garantizar la calidad y el rendimiento de los algoritmos. 
	
</p>

## 🔍 Fase de preprocesamiento de datos

<p>
Para asegurar que los datos sean aptos para el modelado, se realizaron los siguientes pasos:

**1- Carga de Datos:**  se utilizó pandas para cargar el dataset desde un archivo CSV.

**2- Manejo de Valores Faltantes:** se reemplazaron los valores NaN por la media de la columna correspondiente utilizando SimpleImputer de sklearn.

**3- Codificación de Variables Categóricas:** se aplicó OneHotEncoder para convertir variables categóricas en representaciones numéricas y la variable objetivo (Purchased) se transformó a valores binarios (0 y 1).

**4- División del Dataset:** los datos fueron divididos en conjuntos de entrenamiento y prueba con train_test_split, utilizando un 80% para entrenamiento y un 20% para pruebas.

**5- Escalado de Variables:** se aplicó StandardScaler para normalizar los valores numéricos y mejorar la estabilidad de los modelos.

</p>

## 📎 Modelos Implementados

<p>

1️⃣ **Regresión Lineal Simple**: este modelo busca establecer una relación lineal entre una variable independiente y una variable dependiente. Se aplicó para predecir salarios en función de los años de experiencia.

Pasos:

- Se entrenó un modelo de regresión lineal simple con LinearRegression de sklearn.
- Se dividieron los datos en entrenamiento y prueba.
- Se realizaron predicciones y se visualizaron los resultados mediante gráficos de dispersión.

2️⃣ **Regresión Lineal Múltiple**: este modelo extiende la regresión lineal simple para incluir múltiples variables predictoras. Se utilizó para predecir beneficios de startups en función de diferentes factores.

Pasos:

- Se transformaron las variables categóricas en variables dummies.
- Se implementó LinearRegression para entrenar el modelo.
- Se aplicó la técnica de Eliminación hacia atrás con statsmodels para optimizar el modelo y seleccionar las variables más relevantes.

3️⃣ **Regresión Polinómica**: este modelo es una extensión de la regresión lineal que permite capturar relaciones no lineales entre las variables.

Pasos:

- Se utilizó PolynomialFeatures para transformar la variable independiente en términos polinomiales.
- Se entrenó un modelo de LinearRegression sobre estos nuevos términos.
- Se visualizaron los resultados comparando el modelo polinómico con el modelo de regresión lineal simple.

4️⃣ **Regresión con Árboles de Decisión**: este modelo utiliza árboles de decisión para realizar predicciones basadas en divisiones sucesivas de los datos.

Pasos:

- Se entrenó un modelo de DecisionTreeRegressor.
- Se realizó la predicción de valores específicos.
- Se graficaron los resultados para visualizar cómo el modelo segmenta los datos en intervalos.

5️⃣ **Support Vector Regression (SVR)**: este modelo utiliza máquinas de soporte vectorial para encontrar la mejor función de ajuste dentro de un margen de tolerancia.

Pasos:

- Se aplicó escalado de variables con StandardScaler.
- Se entrenó un modelo de SVR con un kernel radial (rbf).
- Se realizó la predicción de nuevos valores y se compararon los resultados.


</p>

## 👾 Razón de lo realizado: 

#### Curso de formación en Machine Learning - Udemy - 2022


