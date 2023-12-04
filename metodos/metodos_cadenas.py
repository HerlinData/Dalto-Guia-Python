cadena1 = "Hola,Maquina,Como,Estas"
cadena2 = "Bien"

# Convierte a mayusculas
mayusc = cadena1.upper()

# Convierte a minusculas
minusc = cadena1.lower()

# Primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

# Buscamos una cadena en otra cadena, si no hay coincidencia devuelve -1
busqueda_find = cadena1.find("a")

# Buscamos una cadena en otra cadena, si no hay coincidencia lanza una excepción
busqueda_index = cadena1.index("C")

# Si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

# Si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

# Contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencia = cadena1.count("la ma")

# Contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

# Verificamos si una cadena empieza con un caracter en específico, si es asi devuelve True
empieza_con = cadena1.startswith("H")

# Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("s")

# Si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace(",", " ")

# Separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(busqueda_index)