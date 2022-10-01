'''
NAME
	CadProteicas.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Encuentra las cadenas proteicas de archivo de ADN dado e imprime la mas larga

CATEGORY
	Genomic Sequence
    
USAGE
    py CadProteicas.py -f (Direccion)

'''

from gzip import READ
from pickle import TRUE
from xmlrpc.client import TRANSPORT_ERROR
from Bio.Seq import Seq
from Bio.SeqUtils import nt_search
import argparse
from email.mime import base
import warnings
warnings.filterwarnings("ignore")

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


# Sacamos la posicion de los codones de inicio y los guardamos en results
sec = Seq(sec)
results = []
results.append( (nt_search(str(sec), 'ATG'))[1::] )
results.append( (nt_search(str(sec.reverse_complement()), 'ATG'))[1::] ) 

i=0
ProtF = ''

# Se calcula la longitud de cada cadena proteica y se comparan
while i < 2:

    for CodonIn in results[i]:

        if i == 0:
            TempProt = ((sec[CodonIn::]).translate(to_stop=TRUE))
            if len(TempProt) > len(ProtF):
                ProtF = TempProt
        else:
            TempProt = (( sec.reverse_complement()[CodonIn::] ).translate(to_stop=TRUE))
            if len(TempProt) > len(ProtF):
                ProtF = TempProt
    i+=1

# Se imprime el resultado
print(ProtF)