with open("archivos\\texto_de_dalto.txt","w",encoding="UTF-8") as archivo:
    
    # Sobreescribiendo el archivo
    #archivo.write("jajajjajaja te la recontra teclee")
    
    # Agregando 2 lineas con writelines
    archivo.writelines(["Hola maestro, ¿como andas?\n","Misericordia\n"])
    
    # Agregando otras 2 lineas
    archivo.writelines(["Hola locoo, ¿por qué dijiste eso?\n","Misericordia"])