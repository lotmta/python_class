# Se abre el archivo y se saca su longitud sin el salto de linea \n
file_name = input("introduce ruta y nombre de tu archivo: ")
file = open(file_name)
file_content = file.read().rstrip("\n")
longitud = len(file_content)

# Se saca el porcentaje de la secuencia y se imprime a pantalla
print(f"Porcentajes de la secuencia: '{file_content}'")
print(f"AT = {((file_content.count('A') + file_content.count('T')) / longitud) * 100} %")
print(f"GC = {((file_content.count('G') + file_content.count('C')) / longitud) * 100} %")

file.close()
