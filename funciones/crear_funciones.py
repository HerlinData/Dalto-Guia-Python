
"""# Creando una función simple
def saludar():
    print("Hola Isaac, mi maestro ¿Cómo andas?")
    
# Ejecutando la funcion simple
saludar()"""

# Crear una funcion que tenga parametro
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "traka"
    print(f"Hola {nombre}, mi {adjetivo} ¿Cómo andas?")
    

saludar("Pedro","Hombre")
saludar("Camila","Mujer")
saludar("Fran","raretee")

# Crear una función que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña,num

# # Desempaquetando la función
# password, primer_numero = crear_contraseña_random(981)

# # Mostrando los resultados obtenidos y los datos utilizados para obtenerlo
# print(f"Tu contraseña nueva es: {password}")
# print(f"El número utilizado para crearla fue: {primer_numero}")


