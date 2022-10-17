'''
NAME
	resumen.py
    
VERSION
    1.1
    
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

# Definimos la funcion
def resumen(file, genes):

    # Pasamos la info a gb
    for gb in SeqIO.parse(file, 'genbank'):

        # Imprimimos los datos generales del archivo
        print(f'Organismo:  {gb.features[0].qualifiers["organism"][0]}')
        print(f'Fecha:  {gb.annotations["date"]}')
        print(f'Pais:   {gb.features[0].qualifiers["country"][0]}')
        print(f'Isolado:    {gb.features[0].qualifiers["isolation_source"][0]}')
        
        # Se usa x para imprimir el "Gen_1","Gen_2". Lo pone en el orden en que se encuentran, no en el orden introducido
        x= 0
        # Pasamos a los datos de cada gen
        for ft in gb.features:

            if ft.type == 'CDS':

                # Checamos si el CDS en el que estamos es de uno de los genes en nuestro vector
                if ft.qualifiers['gene'][0] in genes:
                    x+=1

                    # Imprimimos los datos de nuestro gen
                    print(f"Gen_{x}:    {ft.qualifiers['gene'][0]}")

                    print(f'ADN:    {gb.seq[ft.location.nofuzzy_start:ft.location.nofuzzy_end]}')
                    print(f'ARN:    {gb.seq[ft.location.nofuzzy_start:ft.location.nofuzzy_end].transcribe()}')
                    print(f'Proteina:   {ft.qualifiers["translation"][0]}')

# Pasamos los genes a un vector
genes = args.genes.split(",")

resumen(args.file, genes)