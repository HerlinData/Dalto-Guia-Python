import pandas as pd

# Usando la función read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

# Obteniendo los datos de la columna nombre
nombres = df["Nombre"]

# Ordenando el dataframe por la edad
df_ordenado_ascendente = df.sort_values("Edad")

# Ordenando de forma descendente
df_ordenado_descendente = df.sort_values("Edad",ascending=False)

# Concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

# Accediendo a la primer fila con head()
primeras_filas = df.head(0)

# Accediendo a las últimas 3 filas con tail()
ultimas_filas = df.tail(3)

# Accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

# Obteniendo data estadística del dataframe
df_info = df.describe() ###########GUCHII

# Accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"Edad"] ####GUCHII

# Accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2] ####GUCHII

# Accediendo a todos los apellidos con loc
apellidos = df.loc[:,"Apellido"]

# Accediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]

# Accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

# Accediendo a filas con edad mayor a 30
mayor_que_30 = df.loc[df["Edad"]<30,:]

print(df_concatenado )











#cadena = "0123456789" #
#print(cadena[2:7])    # Ordenar segun queramos


