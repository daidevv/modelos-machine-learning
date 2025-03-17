#Regresion lineal multiple

#Importamos el dataset
dataset = read.csv("50_Startups.csv")

#Transformación (codificacion) de datos categoricos a numericos

dataset$State = factor(dataset$State, 
                         levels = c("New York", "California", "Florida"),
                         labels = c(1, 2, 3)
)



#Division de los datos para la fase de entrenamiento y para la fase de testing
install.packages("caTools")
library(caTools)

set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

#Ajuste del modelo de regresión lineal múltiple con el conjunto de entrenamiento

regression = lm(formula = Profit ~ .,
                data = training_set)

#Predecimos los resultados con el conjunto de testing
y_pred = predict(regression, newdata = testing_set)

# Construcción de un modelo óptimo con el método de la Eliminación hacia atrás
SL = 0.05
regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
                data = dataset)
summary(regression)


regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
                data = dataset)
summary(regression)


regression = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
                data = dataset)
summary(regression)


regression = lm(formula = Profit ~ R.D.Spend,
                data = dataset)
summary(regression)










