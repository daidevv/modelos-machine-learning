#Plantilla de pre procesado de datos -- Datos faltantes

# Importamos el Dataset
dataset = read.csv("Data.csv")

#Tratamiento de los valores NA -Tomamos primero la columna edad
#y calculamos la media, luego hacemos lo mismo con la columna salario

dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)


dataset$Salary = ifelse(is.na(dataset$Salary), 
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

