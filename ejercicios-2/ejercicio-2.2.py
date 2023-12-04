# Creando una función que nos devuelve los números primos 
# Entre 0 y el argumento que pasamos

# Crear una función que verifique si un número es primo
def es_primo(num):
    # Verificamos que el número pasado no pueda dividirse
    # Por ningún número entre 2 y ese mismo número -1
    for i in range(2,num-1):
        # Si el divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
    # Si termina el bucle, significa que no fue divisible entonces es primo
    return True


# Creando función que retorne una lista con todos los primos
def primos_hasta(num):
    # Creamos la lista
    primos =  []
    for i in range(1,num+1):
        # Verificamos si el valor es primo
        resultado = es_primo(i)
        # En caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
        
    # Devolvemos la lista
    return primos

# Creamos el resultado llamando a la función y lo mostramos
resultado = primos_hasta(13)
print(resultado)