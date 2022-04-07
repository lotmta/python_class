file = open("data/4_input_adapters.txt")

contenido = file.read()
lineas = contenido.split("ATTCGATTATAAGC")
file.close()
for linea in lineas:
    print(linea)
