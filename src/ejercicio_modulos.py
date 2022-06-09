'''
NAME
	ejercicio_modulo.py

VERSION
    1.21

AUTHOR
	Lot Hernandez

DESCRIPTION
    Da el porcentaje de un cierto aminoacido de una secuencia dada o de GC y AT en una secuencia dada

CATEGORY
	Genomic Sequence

USAGE

     ejercicio_modulos.py -sec [secuencia] -a [aminoacido] ( -v [motif] )
     ejercicio_modulos.py -sec [secuencia] -n ( -v [motif] )

     Si se va a usar direccion de un archivo con secuencia:

     ejercicio_modulos.py -sec [direccion] -a [aminoacido] -f ( -v [motif] )
     ejercicio_modulos.py -sec [direccion] -n -f ( -v [motif] )


'''

import PROTEINtools
import DNAtools
import argparse
import re

parser = argparse.ArgumentParser(
    description="Da el porcentaje de AT y GC de una secuencia o el porcentaje de un cierto aminoacido de una secuencia")

parser.add_argument("-sec", "--secuencia",
                    help="Introduce tu secuencia, ya sea de aminoacidos o de nucleotidos. O en caso que se use -f, introduce la direccion del archivo con tu secuencia",
                    required=True)
parser.add_argument("-f", "--file",
                    help="Introduce si tu secuencia se encuentra en un archivo, para que lo que introduzcas con -sec se use como direccion a un archivo",
                    action="store_true",
                    required=False)
parser.add_argument("-a", "--aminoacidos",
                    help='Introduce si quieres sacar el porcentaje de un(os) cierto(s) aminoacido(s), introduce ese(estos) aminoacido(s). Ej. "A,G,R"  Ej. "H"  Ej. "L,M" ',
                    required=False)
parser.add_argument("-n", "--nucleotidos",
                    help="Introduce si quieres sacar el porcentaje de AT y GC, no introduzcas nada mas",
                    action="store_true",
                    required=False)
parser.add_argument("-v", "--verifica",
                    help='Introduce si quieres verificar que tu secuencia tenga un cierto motif, introduce el motif. Ej. "ATGC" ',
                    required=False)


args = parser.parse_args()

# Si se uso -a y -n se le notifica al usuario
if (args.aminoacidos and args.nucleotidos):
    print("No puedes usar -a y -n, usa solo el que corresponda a tu tipo de secuencia")
    quit()


# Si se uso -f se trata de abrir el archivo
if(args.file):

    try:
        # Se trata de abrir el archivo, si no existe se cierra el programa. Se guardan los contenidos del archivo en sec
        file_name = args.secuencia
        file = open(file_name)
        sec = file.read().rstrip("\n").upper()

        # Se cierra el archivo
        file.close()
    except IOError:
        print("Error: No se encontro el archivo")
        quit()
else:

    sec = args.secuencia


# Si se uso -v se checa que el motif este en la secuencia
if(args.verifica):
    if(re.search(args.verifica, sec)):
        print("Se encontro el motif")
    else:
        print("No se encontro el motif")


# Si se uso -a se saca el porcentaje de aminoacido
if(args.aminoacidos):
    Amino = (args.aminoacidos).split(",")
    for A in Amino:
        res = PROTEINtools.paminoacidos(sec, A)
        print(f"{A} = {res}%")
    quit()

# Si se uso -n se saca el porcentaje de nucleotidos
if(args.nucleotidos):
    res = DNAtools.pATGC(sec)
    print(f"AT = {res[0]}%\nGC = {res[1]}%")
    quit()

if(not args.verifica):
    # Si no se uso ni -n ni -a ni -v se le notifica al usuario
    print("\nDebes usar -a o -n o -v, dependiendo de que quieres que se saque de tu secuencia")
    print("\n-a si es una secuencia de aminoacidos, -n si es una secuencia de nucleotidos")
    print("\n-v si quieres checar si un motif se encuentra en tu secuencia\n")
