


# Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio" ]):"jajaja"}

# Creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])

# Creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"],"No se")



