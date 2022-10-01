'''
NAME
	CodFast.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Encuentra los codones de los 6 marcos de lectura de las secuencias de un archivo fasta

CATEGORY
	Genomic Sequence
    
USAGE
    py CodFast.py -f (Direccion)

'''

from pickle import TRUE
from Bio import SeqIO
import argparse
import re
import warnings
warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-f", "--file",
                    help="Introduce la direccion del archivo con tu secuencia",
                    required=True)
args = parser.parse_args()

dicc = SeqIO.to_dict(SeqIO.parse(args.file, "fasta"))

for sec in dicc:
    i=0
    
    while i <= 1:
        j=1
        while j <= 3:

            print(f">{sec}, Marco de lectura #{j + (3*i)} ")

            if(i == 0):
                for codon in re.findall(r"(.{3})", str(dicc[sec].seq[j-1::])):
                    print(codon, end= ' ')
            else:
                for codon in re.findall(r"(.{3})", str(((dicc[sec].seq).reverse_complement())[j-1::])):
                    print(codon, end= ' ')

            print('\n')

            j+=1
        i+=1


