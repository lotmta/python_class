'''
NAME
	AT_rich.py

VERSION
    1.0

AUTHOR
	Lot Hernandez

DESCRIPTION
    Busca regiones ricas de DNA de una cierta longitud en una secuencia de DNA dada
CATEGORY
	Genomic Sequence

USAGE
    py AT_rich.py -f (Direccion) -s (Longitud)
'''
import argparse
from email.mime import base
import re

parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-s", "--seccion",
                    help="Introduce el tamaño de la región mínima a buscar como región rica en ATs",
                    required=True)
parser.add_argument("-f", "--file",
                    help="Introduce la direccion del archivo con tu secuencia",
                    required=True)
args = parser.parse_args()

# Funcion que busca bases ambiguas, en caso de que encuentre las imprime y su posicion
def validacionsec(sec):
    bases = ""

    if re.search("[^ATGC]",sec,re.IGNORECASE ):

        ms = re.finditer("[^ATGC]", sec, re.IGNORECASE)


        print("Se encontro una base ambigua\n")

        for m in ms:

            if not (re.search(f"{m.group()}", bases)):

                bases+= m.group()

                vs = re.finditer(f"{m.group()}", sec, re.IGNORECASE)

                print(f'La base {m.group()} fue encontrada en las posiciones: ',end="" )

                for v in vs:

                    print(f'{v.start()}')

        quit()
    return()


try:
    # Se trata de abrir el archivo, si no existe se cierra el programa. Se guardan los contenidos del archivo en sec
    file_name = args.file
    file = open(file_name)
    sec = file.read().rstrip("\n").upper()

    # Se cierra el archivo
    file.close()
except IOError:
    print("Error: No se encontro el archivo")
    quit()

# Se llama la funcion
validacionsec(sec)

s = args.seccion

# Se busca la region rica en AT de la longitud especificada
if re.search("[AT]{"+s+",}", sec, re.IGNORECASE):

    # Si se encuentran, se imprime su posicion
    ms = re.finditer("[AT]{"+s+",}", sec, re.IGNORECASE)
    for m in ms:
        print(f'Una region alta en AT fue encontrada en la posicion {m.span()}' )

else:
    print(f"No se encontro niguna region rica en AT de tamaño {s}")
