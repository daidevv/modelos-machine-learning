#SVR


#Importamos el dataset
dataset = read.csv("Position_Salaries.csv")
dataset =dataset[, 2:3]

#Division de los datos para la fase de entrenamiento y para la fase de testing
#install.packages("caTools")

# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# testing_set = subset(dataset, split == FALSE)

#Escalado de valores num?ricos
# training_set[,2:3] = scale(testing_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])


# Creacion (Ajuste) del Modelo de Regresión con el Conjunto de Datos
install.packages("e1071")
library(e1071)

regression = svm(formula = Salary ~ ., 
                 data = dataset, 
                 type = "eps-regression", 
                 kernel = "radial",
                 cost = 9)
  

# Predicción de nuevos resultados con SVR
y_pred = predict(regression, newdata = data.frame(Level = 6.5))


# Visualización del modelo

# install.packages("ggplot2")
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = dataset$Level, y = predict(regression, 
                                        newdata = data.frame(Level = dataset$Level))),
            color = "blue") +
  ggtitle("Predicción SVR") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")