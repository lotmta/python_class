'''
NAME
	NCBI25.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    articulos_tit: Da titulos e IDs de articulos que se encontraron con buscar_db
    extraer_y_guardar: Da un vector con todos los articulos que citaron alguno de todos los articulos dados por articulos_tit.
                       De estos articulos da su ID, titulo y abstract. Puede tardar mucho dependiendo del numero de articulos
                       que se le den. 

CATEGORY
	Genomic Sequence
    
USAGE
    py NCBI25.py -t (Termino sin formato) 

'''

from Bio import Entrez
from NCBI18 import buscar_db, crear_termino
import argparse

parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-t", "--termino",
                    help="Introduce el organismo y los genes de este en formato 'Organismo1: Gene1,Gene2 ; Organismo2: Gene3,Gene4' ",
                    required=True)
args = parser.parse_args()

Entrez.email = "lotmateohernandezespinosa@gmail.com"




                    ###############################################################

# ADVERTENCIA, PUEDE TARDAR MUCHO; Aguas con esta funcion, dependiendo de que tan popular sea 
# lo que buscaste puede tardar demasiado en correr ya que crecen exponencialmente las busquedas.
def extraer_y_guardar(Articulos):

    # Sacamos todos los articulos que citaron alguno de los articulos en nuestra lista ( Articulos['IDS'] )
    results = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pubmed", id=Articulos['IDS'], LinkName='pubmed_pubmed_refs'))

    # Inicializamos el vector ArticuloRefs
    # Este vector tendra un elemento por cada articulo de nuestra lista original (Articulos)
    # Cada elemento tendra un vector con el titulo del articulo original y diccionario [TituRefs]
    # Los diccionarios (TituAbstraRef) tendran los IDs, titulos y abstracts de todos los articulos que citan a nuestro articulo original
    ArticuloRefs = []
    i= 0

    # Results es un array, cada elemento de este pertenece a uno de nuestros articulos.
    # Vamos de uno en uno para ver el resultado de cada articulo, que contiene los articulos que lo citan.
    for result in results:

        # Inicializamos el diccionario que tendra el titulo y el vector con diccionarios (Refs)
        TituRefs = {}  
        # Tambien el vector que tendra los diccionarios (TituAbstraRef) donde estara el ID, titulo y abstract de cada articulo
        Refs = []

        # Entramos al diccionario donde estan los IDs de los articulos
        for link in result['LinkSetDb']:
            
            # Checamos si si hay articulos
            if len(link) > 0:
                
                # Vamos articulo por articulo
                for id in link['Link']:
                    
                    # Inicializamos el diccionario que tendra el ID, titulo y abstract de cada articulo
                    TituAbstraRef = {}

                    # Usamos try al hacer efetch de cada ID de cada articulo ya que si va muy rapido el for y hacemos muchos
                    # requests a veces tira error con algunos IDs
                    try:
                        
                        # Hacemos efetch de este articulo
                        Articulo = Entrez.read(Entrez.efetch(db='pubmed', id = id['Id'], api_key = '2c4f67def001c89be6a3d681c1da87fc8409'))

                        # Guardamos el ID de este
                        TituAbstraRef['Id'] = id['Id']

                        # Checamos si tiene abstract disponible
                        if 'abstract' in list(Articulo['PubmedArticle'][0]['MedlineCitation']['Article'].keys()):
                            
                            # Si si tiene lo guardamos
                            TituAbstraRef['Abstract'] = Articulo['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText'][0]
                        else:
                            
                            # Si no tiene en su lugar guardamos 'No abstract'
                            TituAbstraRef['Abstract'] = 'No abstract'
                        
                        # Guardamos el titulo del articulo
                        TituAbstraRef['Titulo'] = Articulo['PubmedArticle'][0]['MedlineCitation']['Article']['ArticleTitle']

                        # Como tituabstraref se reinicia para cada articulo, guardamos su info en nuestro
                        # vector de diccionarios.
                        Refs += [TituAbstraRef]

                    except:
                        pass
                    
            
            # Guardamos el Titulo del articulo original (el que es citado por los demas)
            TituRefs['Titulo'] = Articulos['Titulos'][i]
            # Guardamos la info de los articulos que lo citan
            TituRefs['Referencias'] = Refs
            # Guardamos todo esto en el vector principal, ya que hay varios articulo citados (tantos como se le dan a la funcion)
            ArticuloRefs += [TituRefs]
            
            # El contador es para ver en que articulo original vamos (de los que son citados)
            i+=1

    return(ArticuloRefs)

                    ###############################################################




                    ###############################################################

# Inicializamos nuestra funcion para sacar los titulos de los articulos encontrados
def articulos_tit(Dbs):

    # Se inicializa el diccionario que tendra el titulo e ID de cada uno de los articulos encontrados
    Articulos = {}

    i = 0

    for Db in Dbs:
        
        #Inicializamos el vector que tendra nuestros titulos
        Titus = []

        # Checamos que nuestra busqueda haya tenido resultados en pubmed, que es la base de datos con articulos
        if ('pubmed' in list(Db.keys())):

            # En caso de que si, vamos una por una de las IDs que dio pubmed
            for ID in Db['pubmed']:

                # Sacamos el titulo y lo metemos en nuestro vector de titulos
                Articulo = Entrez.read(Entrez.efetch(db='pubmed', id = ID))
                Titus += [Articulo['PubmedArticle'][0]['MedlineCitation']['Article']['ArticleTitle']]
        
        # Metemos a nuestro vector de titulos al diccionario junto con las IDs
        Articulos['Titulos'] = Titus
        Articulos['IDS'] = Db['pubmed'] 
    
    return(Articulos)

                    ###############################################################


terminos = crear_termino(args.termino)
Dbs = buscar_db(terminos)

Articulos = articulos_tit(Dbs)

ArticuloRefs = extraer_y_guardar(Articulos)

print(ArticuloRefs)

