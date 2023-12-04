# Importando un modulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar

# Desde ese modulo, importamos dos funciones y les cambiamos el nombre
from funciones_buenas.modulo_saludar import saludar as saludar_normal, saludar_raro as saludar_como_coscu
#import modulo_saludar as m_saludar

# Creamos las variables con los saludos
saludo = saludar_normal("Lucas")
saludar_raro = saludar_como_coscu("Frank")

# Mostramos los resultados
print(saludo)
print(saludar_raro)

# Para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))

# Accedemos al nombre de este modulo
print(__name__)

# Accedemos al nombre del modulo llamada
#print(m_saludar.__name__)