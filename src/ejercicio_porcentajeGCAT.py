'''
NAME
	ejercicio_porcentajeGCAT.py
    
VERSION
    1.1
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Da el porcentaje de GC y AT de una secuencia en un archivo dado
        
CATEGORY
	Genomic Sequence
    
USAGE
'''


try:
    # Se trata de abrir el archivo, si no existe se cierra el programa
    file_name = input("introduce ruta y nombre de tu archivo: ")
    file = open(file_name)
except IOError:
    print("Error: No se encontro el archivo")
    quit()

# Se guarda el contenido del archivo en file_content, se eliminan los saltos de linea y se pone todo en mayusculas
file_content = file.read().rstrip("\n").upper()
longitud = len(file_content)

try:
    # Se checa si hay N's en la secuencia
    if file_content.count("N") > 0:
        raise ValueError()
except ValueError:
    print(f"Error: La secuencia tiene {file_content.count('N')} N's")
    quit()


# Se saca el porcentaje de la secuencia y se guarda en variables
AT = ((file_content.count('A') + file_content.count('T')) / longitud) * 100
GC = ((file_content.count('G') + file_content.count('C')) / longitud) * 100

# Se imprime el reslutado
print(f"Porcentajes de la secuencia: '{file_content}'")
print(f"{AT} %")
print(f"{GC} %")

# Cierro el archivo
file.close()
