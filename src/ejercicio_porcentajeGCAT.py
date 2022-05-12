'''
NAME
	ejercicio_porcentajeGCAT.py
    
VERSION
    1.2
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Da el porcentaje de GC y AT de una secuencia en un archivo dado
        
CATEGORY
	Genomic Sequence
    
USAGE
'''


from decimal import DivisionByZero
import argparse

parser = argparse.ArgumentParser(
    description="Da el porcentaje de GC y AT de una secuencia en un archivo dado")

parser.add_argument("-i", "--input",
                    help="Direccion del archivo con tu secuencia",
                    required=True)

parser.add_argument("-o", "--output",
                    help="Nombre y direccion del archivo que se creara con el resultado",
                    required=False)

args = parser.parse_args()

try:
    # Se trata de abrir el archivo, si no existe se cierra el programa
    file_name = args.input
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

try:
    # Se saca el porcentaje de la secuencia y se guarda en variables
    AT = ((file_content.count('A') + file_content.count('T')) / longitud) * 100
    GC = ((file_content.count('G') + file_content.count('C')) / longitud) * 100
except ZeroDivisionError:
    print("Error: Tu archivo esta vacio")
    quit()

if not args.output:
    # Se imprime el reslutado
    print(f"Porcentajes de la secuencia: '{file_content}'")
    print(f"{AT} %")
    print(f"{GC} %")

else:
    # Se abre el archivo output
    output = open(args.output, "w")
    output.write(f"Porcentajes de la secuencia: '{file_content}'")
    output.write(f"\n{AT} %")
    output.write(f"\n{GC} %")

    # Cierro el archivo
file.close()
