# Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")

# Convertir a string los datos de una columna
df["Edad"] = df["Edad"].astype(str)

# Mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df["Edad"][0]))

# Reemplazando los datos "Dalto" por "Maestro"
df["Apellido"].replace("Dalto","Maestro",inplace=True)

# Eliminando las filas con datos faltantes
df= df.dropna()

# Eliminando las filas repetidas
df = df.drop_duplicates()

# Creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")


