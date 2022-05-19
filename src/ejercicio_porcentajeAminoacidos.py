'''
NAME
	ejercicio_porcentajeAminoacidos.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Da el porcentaje de un cierto aminoacido de una secuencia dada
        
CATEGORY
	Genomic Sequence
    
USAGE
'''

import argparse

parser = argparse.ArgumentParser(
    description="Da el porcentaje de un aminoacido especifico de una secuencia dada")

parser.add_argument("-sec", "--secuencia",
                    help="Tu secuencia",
                    required=True)

parser.add_argument("-a", "--aminoacido",
                    help="El aminoacido del que quieres saber el porcentaje",
                    required=True)
args = parser.parse_args()

# Se meten los argumentos a variables
sec = args.secuencia
amin = args.aminoacido


# Se checa que la longitud de secuencia no sea 0 y que solo se haya pedido el porcentaje de 1 aminoacido
if(len(sec) == 0):
    print("Error: No introdujiste una secuencia")
    quit()
if(len(amin) != 1):
    print("Error: Solo introduce un aminoacido")
    quit()


# Funcion con la que se saca el porcentaje
def porcentajeamin(sec, amin):
    porcentaje = round(((sec.upper().count(amin.upper())) / len(sec)) * 100)
    return(porcentaje)


print(
    f"El porcentaje de {amin} en tu secuencia es:\n{porcentajeamin(sec, amin)} %")
