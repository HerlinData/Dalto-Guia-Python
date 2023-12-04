
# Creando las listas
frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "Hola Dalto"
numeros = [2,5,8,10]

# Evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"Me voy a comer una {fruta}")
    
print("---------------------------")
    
#Evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera":
        break
else:
    print("terminado")
print("---------------------------")

# Recorrer una cadena de texto
for letra in cadena:
    print(letra)

# For en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)
