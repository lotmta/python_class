'''
NAME
	fastqcheck.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Da un archivo con las secuencias que superan el umbral de calidad dado

CATEGORY
	Genomic Sequence
    
USAGE
    py fastqcheck.py -f (Direccion) (Umbral)

'''

from Bio import SeqIO
import argparse


parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-f", "--file",
                    help="Introduce la direccion del archivo con tu secuencia",
                    required=True)
parser.add_argument("-u", "--umbral",
                    help="Introduce el valor de calidad que tus secuencias deben superar",
                    required=True)               
args = parser.parse_args()

# Abrimos el archivo output
output = open("results.txt", "w")

# Se empieza el contador
n = 0

# Se checa si superan el umbral
for sec in SeqIO.parse(args.file, 'fastq'):
    
    if(all(x > int(args.umbral)    for x in sec.letter_annotations["phred_quality"])):
        output.write(f'{sec.id}\n{str(sec.seq)}\n')

        n+=1
print(n)

output.close


