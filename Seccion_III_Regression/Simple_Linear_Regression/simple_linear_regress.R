#Instalamos la libreria ggplot2 para la representacion gráfica
install.packages("ggplot2")
library(ggplot2)


# Plantilla para el pre procesado de datos

dataset = read.csv("Salary_Data.csv")

#División de los datos para la fase de entrenamiento y la fase de testing

install.packages("caTools")
library(caTools)

set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)


#Ajustamos el modelo de regresión lineal simple con el conj. de entrenamiento
#Uso de la funcion lm(linear model) para crear automaticamente el modelo lineal

regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

#Predecimos resultados con el conj. de datos de entrenamiento 
#Creamos un vector de resultados y usamos la funcion predict para realizar predicciones

y_pred = predict(regressor, newdata = testing_set)
 
#Agregamos las "capas de representacion" de ggplot + 


ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = "red") + #pongo + para seguir agregando componentes
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
              colour = "blue") +
  ggtitle("Sueldo vs. Años de experiencia (conj. de entrenamiento)") +
  xlab("Años de experiencia") +
  ylab("Sueldo (en $)")
  

#Visualización de los resultados en el conjunto de testing
ggplot() +
  geom_point(aes(x = testing_set$YearsExperience, y = testing_set$Salary),   
             colour = "red") + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = "blue") +
  ggtitle("Sueldo vs. Años de experiencia (conj. de testing)") +
  xlab("Años de experiencia") +
  ylab("Sueldo (en $)")













 