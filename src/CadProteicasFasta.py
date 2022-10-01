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
from Bio import SeqIO
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


# Sacamos la posicion de los codones de inicio y los guardamos en results


for sec in SeqIO.parse(args.file, 'fasta'):
    print(f'>{sec.id}')
    results = []
    results.append( (nt_search(str(sec.seq), 'ATG'))[1::] )
    results.append( (nt_search(str(sec.seq.reverse_complement()), 'ATG'))[1::] ) 

    i=0
    ProtF = ''

    # Se calcula la longitud de cada cadena proteica y se comparan
    while i < 2:

        for CodonIn in results[i]:

            if i == 0:
                TempProt = ((sec.seq[CodonIn::]).translate(to_stop=TRUE))
                if len(TempProt) > len(ProtF):
                    ProtF = TempProt
            else:
                TempProt = (( sec.seq.reverse_complement()[CodonIn::] ).translate(to_stop=TRUE))
                if len(TempProt) > len(ProtF):
                    ProtF = TempProt
        i+=1

    # Se imprime el resultado
    print(ProtF)
