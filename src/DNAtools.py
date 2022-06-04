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
    import DNAtools
    
    DNAtools.pATGC([secuencia])
        

'''

# Funcion con la que se saca el porcentaje


def pATGC(sec):

    porcentajeAT = round(
        (((sec.upper().count("A")) + (sec.upper().count("T"))) / len(sec)) * 100)
    porcentajeGC = round(
        (((sec.upper().count("G")) + (sec.upper().count("C"))) / len(sec)) * 100)
    return(porcentajeAT, porcentajeGC)
