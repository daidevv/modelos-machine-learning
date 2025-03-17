# Script completo de la etapa de preprocesamiento


dataset = read.csv("Data.csv")

#Tratamiento de los valores NA
dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
 

dataset$Salary = ifelse(is.na(dataset$Salary), 
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)

#Codificaci?n de datos categoricos a num?ricos.
dataset$Country = factor(dataset$Country, 
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1, 2, 3)
                         )


dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0, 1)
                           )
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




