'''
NAME
	ejercicio_count_nucleotide_input.py
    
VERSION
    1.1
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
	Cuenta los nucleotidos de una secuencia introducida
    
CATEGORY
	Genomic Sequence
    
USAGE
'''

# Se introduce la secuencia y todo se pone en mayusculas por si la secuencia se paso en minusculas
dna = input("Introduce tu secuencia de DNA:\n").upper()

try:
    # Se checa si hay N's en la secuencia
    if dna.count("N") > 0:
        raise ValueError()
except ValueError:
    print(f"Error: La secuencia tiene {dna.count('N')} N's")
    quit()

    # Se cuenta la cantidad de cada nucleotido y se guarda en variables
A = dna.count('A')
C = dna.count('C')
G = dna.count('G')
T = dna.count('T')

# Se imprime el resultado
print(
    f"Cantidad de A:{A} C:{C} G:{G} T:{T} ")
