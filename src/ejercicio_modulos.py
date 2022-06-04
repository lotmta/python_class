'''
NAME
	ejercicio_modulo.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Da el porcentaje de un cierto aminoacido de una secuencia dada o de GC y AT en una secuencia dada
        
CATEGORY
	Genomic Sequence
    
USAGE
     
     ejercicio_modulos.py -sec [secuencia] -a [aminoacido]
     ejercicio_modulos.py -sec [secuencia] -n       

'''

import PROTEINtools
import DNAtools
import argparse

parser = argparse.ArgumentParser(
    description="Da el porcentaje de AT y GC de una secuencia o el porcentaje de un cierto aminoacido de una secuencia")

parser.add_argument("-sec", "--secuencia",
                    help="Introduce tu secuencia, ya sea de aminoacidos o de nucleotidos",
                    required=True)

parser.add_argument("-a", "--aminoacidos",
                    help="Introduce si quieres sacar el porcentaje de un cierto aminoacido, introduce ese aminoacido",
                    required=False)
parser.add_argument("-n", "--nucleotidos",
                    help="Introduce si quieres sacar el porcentaje de AT y GC, no introduzcas nada mas",
                    action="store_true",
                    required=False)

args = parser.parse_args()

# Si se uso -a y -n se le notifica al usuario
if (args.aminoacidos and args.nucleotidos):
    print("No puedes usar -a y -n, usa solo el que corresponda a tu tipo de secuencia")
    quit()

sec = args.secuencia

# Si se uso -a se saca el porcentaje de aminoacido
if(args.aminoacidos):
    A = args.aminoacidos
    res = PROTEINtools.paminoacidos(sec, A)
    print(f"{res}%")
    quit()

# Si se uso -n se saca el porcentaje de nucleotidos
if(args.nucleotidos):
    res = DNAtools.pATGC(sec)
    print(f"AT = {res[0]}%\nGC = {res[1]}%")
    quit()

# Si no se uso ninguno se le notifica al usuario
print("Debes usar -a o -n, dependiendo de que quieres que se saque de tu secuencia")
