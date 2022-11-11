'''
NAME
	NCBI18.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    crear_termino: Le da formato a un termino para herramientas Entrez 
    buscar_db: Dados terminos de busqueda, encuentra Ids en base de datos con informacion sobre el tema

CATEGORY
	Genomic Sequence
    
USAGE
    py NCBI18.py -t (Termino sin formato) 

'''

from Bio import Entrez
from pprint import pprint 
import argparse
import re

parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-t", "--termino",
                    help="Introduce el organismo y los genes de este en formato 'Organismo1: Gene1,Gene2 ; Organismo2: Gene3,Gene4' ",
                    required=True)
args = parser.parse_args()

Entrez.email = "lotmateohernandezespinosa@gmail.com"

# Se define la funcion para darle formato al termino
def crear_termino(inpts):

    # Inicializamos la lista donde guardaremos los terminos, donde cada elementp corresponde a un organismo y sus genes correspondientes 
    terminos=[]

    # Hacemos un for para que el formateo se repita para cada organismo, los organismos esan separados por un ; por eso el split
    for inpt in inpts.split(';'):

        # Separamos los genes del organismo y metemos a este en la variable $termino
        inpt = inpt.split(":")
        termino = inpt[0] + "[Orgn] AND ("

        # Separamos cada gen para introducirlos de uno a uno en $termino con el formato adecuado
        i = True
        for gen in inpt[1].replace(" ","").split(','):
            if i:
                termino += gen+'[Gene]'
            else:
                termino += " OR " + gen+'[Gene]' 
            i = False

        termino += ")"

        # Metemos lo de termino al vector
        terminos += [termino]

    return(terminos)


# Se define la funcion para buscar en las bases de datos
def buscar_db(terminos):

    # Inicializamos la lista donde guardaremos los ids de las bases de datos segun el organismo, sera una lista de diccionarios de listas
    DbIDS = []

    # Hacemos este for para repetir todo por cada organismo
    for termino in terminos:

        # Buscamos los datos
        record = Entrez.read(Entrez.egquery(term = termino))

        # Inicializamos la lista que tendra las bases de datos en donde si hay informacion, Count > 1
        # Tambien el diccionario donde guardaremos la lista de IDs de cada base de datos que paso el criterio
        DictDbs = {}
        Dbs=[]

        # Checamos que bases de datos pasan nuestro criterio y las guardamos en $DBs
        for row in record["eGQueryResult"]:
            if (row["Count"] != "Error"):
                if(int(row["Count"]) > 1):
                    Dbs += [row["DbName"]]
        
        # Ahora para cada base de datos guardamos la lista con los IDS
        for Db in Dbs:
            DictDbs[Db] = Entrez.read(Entrez.esearch(db= Db, term=termino))["IdList"]
        
        # Este diccionario lo guardamos en la lista que iniciamos al inicio, esto para que se separen las bases de datos y IDS segun el organismo
        DbIDS+= [DictDbs]

    return(DbIDS)

termino = args.termino

termino = crear_termino(termino)

Dbs = buscar_db(termino)
