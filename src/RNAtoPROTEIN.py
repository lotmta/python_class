'''
NAME
	RNAtoPROTEIN.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Transcribe una secuencia de RNA a una de aminoacidos

CATEGORY
	Genomic Sequence
    
USAGE
    py RNAtoPROTEIN.py -f (Direccion)

'''
import argparse
from email.mime import base

parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-f", "--file",
                    help="Introduce la direccion del archivo con tu secuencia",
                    required=True)
args = parser.parse_args()

try:
    # Se trata de abrir el archivo, si no existe se cierra el programa. Se guardan los contenidos del archivo en sec
    file_name = args.file
    file = open(file_name)
    sec = file.read().rstrip("\n").upper().replace("U", "T")

    # Se cierra el archivo
    file.close()
except IOError:
    print("Error: No se encontro el archivo")
    quit()

# Diccionario con el codigo genetico
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
    'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
    'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
    'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
    'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
    'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# Sacamos el numero de codones
num = ((len(sec))//3)

# Inicializamos las variables necesarias
prot= ''
j = 0
w = 3

# Se transcribe de RNA a proteina
for i in range(num):
    prot += gencode[(sec[j:w])]
    j+=3
    w+=3

# Se imprime el resultado
print(prot)
