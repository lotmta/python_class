'''
NAME
	ejercicio_formateo_fasta.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Cambia el formato de un archivo a uno fasta, pone todo en mayusculas y elimina los -. El archivo input esta en data (dna_sequences.txt) y el output estara en results (secuencia_formato_fasta.txt)
        
CATEGORY
	Genomic Sequence
    
USAGE
'''

# Se abre el archivo y se separa por lineas en una lista
file = open("data/dna_sequences.txt")
lineas = file.read()
lineas = lineas.split("\n")

# Se abre el archivo output
output = open("results/secuencia_formato_fasta.txt", "w")

# Se abre el for donde cada linea va a ser separada por seqid y la secuencia en si, primero se hace un write del seqid con su > y un salto de linea. Despues se hace otro write donde se añade la secuencia y un salto de linea, asegurandonos de que todo este en mayusculas (y si no cambiandolo a mayusculas) y que no tenga --- (borrandolos si es que hay)
for linea in lineas:
    seqid = linea.split(" ")
    output.write(f">{seqid[0]}\n")
    output.write(f"{seqid[-1].upper().replace('-','')}\n\n")
