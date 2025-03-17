#Plantilla base preprocesado

#Importamos el dataset
dataset = read.csv("Data.csv")

#Divisi?n de los datos para la fase de entrenamiento y para la fase de testing
install.packages("caTools")
library(caTools)

set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

#Escalado de valores num?ricos
training_set[,2:3] = scale(testing_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])