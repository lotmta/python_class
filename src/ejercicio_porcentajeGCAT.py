file_name = input("introduce ruta y nombre de tu archivo: ")
file = open(file_name)
file_content = file.read().rstrip("\n")
longitud = len(file_content)

print(f"La longitud de la secuencia '{file_content}' es: {longitud}")
