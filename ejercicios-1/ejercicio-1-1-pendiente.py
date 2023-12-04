#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duración

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = round(100 - dalto_curso * 1000 / otros_cursos_max / 10, 2)
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#Calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = round(100 - otros_cursos_promedio * 1000 // crudo_promedio / 10, 2)
tiempo_vacio_dalto = round(100 - dalto_curso * 1000 // crudo_dalto / 10, 2)


#Mostrando las diferencias de duración (Ejercicio A)

print("----------------------------------")
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el más rápido")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el más lento")
print(f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio")
print("----------------------------------")

#Mostrando la cantidad de espacios vacios que se remueven (Ejecicio B)
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este curso elimino {tiempo_vacio_dalto}% de tiempo vacio")
print("----------------------------------")

#Mostrando diferencias si los cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a ver {round(otros_cursos_promedio * 100 / dalto_curso / 10, 2)} horas de otros cursos") #
print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 / otros_cursos_promedio / 10} horas de este curso") # 
print("----------------------------------")





