'''
NAME
	resumen.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Dado un archivo genbank y los genes deseados, da un resumen de estos

CATEGORY
	Genomic Sequence
    
USAGE
    py resumen.py -f (Direccion) -g (Genes)
    py resumen.py -f data.gb -g L,M,P

'''

from Bio import SeqIO
import argparse


parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-f", "--file",
                    help="Introduce la direccion del archivo con tu secuencia",
                    required=True)
parser.add_argument("-g", "--genes",
                    help="Introduce los genes deseados",
                    required=True)

args = parser.parse_args()

def resumen(file, genes):

    for gb in SeqIO.parse(file, 'genbank'):
        print(f'Organismo:  {gb.features[0].qualifiers["organism"][0]}')
        print(f'Fecha:  {gb.annotations["date"]}')
        print(f'Pais:   {gb.features[0].qualifiers["country"][0]}')
        print(f'Isolado:    {gb.features[0].qualifiers["isolation_source"][0]}')
        
        x= 0
        for ft in gb.features:

            if ft.type == 'CDS':
                if ft.qualifiers['gene'][0] in genes:
                    x+=1
                    print(f"Gen_{x}:    {ft.qualifiers['gene'][0]}")

                    print(f'ADN:    {gb.seq[ft.location.nofuzzy_start:ft.location.nofuzzy_end]}')
                    print(f'ARN:    {gb.seq[ft.location.nofuzzy_start:ft.location.nofuzzy_end].transcribe()}')
                    print(f'Proteina:   {ft.qualifiers["translation"][0]}')
genes = args.genes.split(",")

resumen(args.file, genes)