'''
NAME
	ejercicio_eliminar_adaptador.py
    
VERSION
    1.1
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Da la secuencia que esta en data/4_input_adapters.txt en la carpeta results pero sin los primeros 14 caracteres de la primera lista
        
CATEGORY
	Genomic Sequence
    
USAGE
	py ejercicio_eliminar_adaptador.py
'''

# Se abre el archivo y se separa por lineas en una lista
file = open("../data/4_input_adapters.txt")
lineas = file.readlines()

# Se abre el archivo output
output = open("../results/secuencia_sin_adaptador.txt", "w")

# Se cierra el archivo para que no se quede en la memoria
file.close()

# Se abre el for donde por cada linea del input se va a escribir esa misma linea en el output pero sin los primeros 14 caracteres
for linea in lineas:
    output.write(f"{linea[14:]}")

output.close()
