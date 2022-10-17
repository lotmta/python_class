'''
NAME
	genL.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Dado un archivo genbank, da la secuencia, transcripcion y traduccion del gen L

CATEGORY
	Genomic Sequence
    
USAGE
    py genL.py -f (Direccion)

'''

from Bio import SeqIO
import argparse


parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-f", "--file",
                    help="Introduce la direccion del archivo con tu secuencia",
                    required=True)
           
args = parser.parse_args()

# Metemos la info a gb
for gb in SeqIO.parse(args.file, 'genbank'):
    
    # Vamos por cada una de sus features para buscar el CDS del gen L
    for ft in gb.features:

        if ft.type == 'CDS':
            if ft.qualifiers['gene'][0] == 'L':

                # En caso de que sea de tipo CDS y que sea del gen L imprimimos lo pedido
                print(f'Secuencia: {gb.seq[ft.location.nofuzzy_start:ft.location.nofuzzy_end]}\n')
                print(f'Transcripcion: {gb.seq[ft.location.nofuzzy_start:ft.location.nofuzzy_end].transcribe()}\n')
                print(f'Traduccion: {ft.qualifiers["translation"][0]}\n')