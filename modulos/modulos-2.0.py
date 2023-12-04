# Si el modulo estuviera dentro de una carpeta en la misma carpeta "main"
#import funciones_buenas.saludar as m_saludar

import sys

sys.path.append("C:\\Users\\Isaac\\Desktop\\Python_Dalto\\funciones_buenas")
print(sys.path)

import saludar as modulo_saludo

print(modulo_saludo.saludar("Dalto"))