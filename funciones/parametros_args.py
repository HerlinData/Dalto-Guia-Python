# Forma no optima de sumar valores
"""
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
resultado = suma([5,3,9,10,10,10,10,2,11,10,10,10])"""

# Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])


# Lo mismo que arriba, pero utilizando el operador * como parametro (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus números es: {sum(numeros)}"
    
resultado = suma("Lucas",5,3,9,10,20,3)
