'''
NAME
	OFgenbank.py
    
VERSION
    1.1
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Da las fechas, nombres y pais de los organismos de un archivo genbank

CATEGORY
	Genomic Sequence
    
USAGE
    py OFgenbank.py -f (Direccion)

'''

from Bio import SeqIO
import argparse


parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-f", "--file",
                    help="Introduce la direccion del archivo con tu secuencia",
                    required=True)
           
args = parser.parse_args()



# Se imprime la fecha, los nombres y el pais de los organismos en el archivo
for gb in SeqIO.parse(args.file, 'genbank'):
    print(f"Organismo: {gb.annotations['organism']}")
    print(f"Fecha: {gb.annotations['date']}")
    print(f"Pais: {gb.features[0].qualifiers['country']}")



