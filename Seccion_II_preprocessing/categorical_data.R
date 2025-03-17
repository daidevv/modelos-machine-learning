#Plantilla para el preprocesado de datos -- Datos categ?ricos

# Importamos el Dataset
dataset = read.csv("Data.csv")

#Transformación de datos categoricos a numericos

dataset$Country = factor(dataset$Country, 
                         levels = c("France", "Spain", "Germany"),
                         labels = c(1, 2, 3)
)

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", "Yes"),
                           labels = c(0, 1)
)

