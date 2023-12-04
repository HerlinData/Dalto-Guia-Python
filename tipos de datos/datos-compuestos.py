
# Creando una lista (se pueden modificar)
lista = ["Lucas Dalto", "Soy Dalto", True, 1.85]

# Creando una tupla (no pueden modificar)
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85)

#esto es válido
lista[3] = "Maquinola"

# Esto no es valido
#tupla[3] = "Maquinola"

# Creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)

conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85, "Soy Dalto"}

# print(conjunto[3]) -> no puede acceder al elemento


# Creando un diccionario (dict) (la estructura es "key : value" y separamos por comas)
diccionario = {
    "Nombre" : "Lucas Dalto",
    "Canal" : "Soy Dalto",
    "Esta_emocionado" : True,
    "Altura" : 1.85,
    "dato_duplicado" : "SoyDDalto"
}

print(diccionario["Canal"])



