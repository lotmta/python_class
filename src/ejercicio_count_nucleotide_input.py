'''
NAME
	ejercicio_count_nucleotide_input.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
	Cuenta los nucleotidos de una secuencia introducida
    
CATEGORY
	Genomic Sequence
    
USAGE
'''

# Se introduce la secuencia
dna = input("Introduce tu secuencia de DNA:\n")

# Se cuenta la cantidad de cada nucleotido y se imprime
print(
    f"Cantidad de A:{dna.count('A')} C:{dna.count('C')} G:{dna.count('G')} T:{dna.count('T')} ")
