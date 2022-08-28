'''
NAME
	ejercicio_formateo_fasta.py
    
VERSION
    1.1
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Cambia el formato de un archivo a uno fasta, pone todo en mayusculas y elimina los -. El archivo input esta en data (dna_sequences.txt) y el output estara en results (secuencia_formato_fasta.txt)
        
CATEGORY
	Genomic Sequence
    
USAGE
'''


try:
    # Se abre el archivo y se separa por lineas en una lista
    file = open("data/dna_sequences.txt")
    lineas = file.read()
    lineas = lineas.split("\n")
except IOError:
    print("Error: No se encontro el archivo data/dna_sequences.txt")

# Se cierra el archivo para que no se quede en la memoria
file.close()

# Se abre el archivo output
output = open("results/secuencia_formato_fasta.txt", "w")

# Se usa un for para separar el seqid de la secuencia y asegurarnos de que la secuencia este en mayusculas y que no tenga ---.
for linea in lineas:
    seqid = linea.split(" ")
    output.write(f">{seqid[0]}\n")
    output.write(f"{seqid[-1].upper().replace('-','')}\n\n")

# Se cierra el archivo output para que no se quede en la memoria
output.close
