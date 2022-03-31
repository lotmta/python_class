'''
NAME
	ejercicio_fasta.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
	Le da formato fasta a un archivo con secuencia de DNA
    
CATEGORY
	Genomic Sequence
    
USAGE
'''

# Se abre el archivo que contiene la secuencia
file_name = "data/dna.txt"
file = open(file_name)
file_content = file.read().rstrip("\n")

# Se pide el SeqID
SeqID = input("Introduce el identificador de la secuencia: ")

# Se crea el archivo .fasta
file_fasta = open("dna.fasta", "w")
file_fasta.write(f">{SeqID} \n{file_content}")

# Cierro el archivo
file.close()
