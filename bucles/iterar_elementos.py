animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [52,16,14,72]

# Recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animas es igual a : {animal}")

# Recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print (resultado)


# Iterando dos listas del mismo tamaño al mismo tiempo
for numero, animal in zip(numeros, animales):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
      
      
# Forma no optima de recorrer una lista (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
    
# Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es {valor}")
    


# Usando el for/else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")
    

# Todo lo anterior funciona exactamente igual para tuplas y conjuntos
