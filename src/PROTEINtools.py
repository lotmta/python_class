'''
NAME
	PROTEINtools.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Modulo: Da el porcentaje de un cierto aminoacido de una secuencia dada
        
CATEGORY
	Genomic Sequence
    
USAGE
    import PROTEINtools
    
    PROTEINtools.paminoacidos([secuencia], [aminoacido])
        

'''

# Funcion con la que se saca el porcentaje


def paminoacidos(sec, amin):
    sum = 0

    for aminoacido in amin:
        sum += (sec.upper().count(aminoacido.upper()))

    porcentaje = round((sum / len(sec)) * 100)

    return(porcentaje)
