
#sec = input("Introduce tu secuencia de aminoacidos: ")
#amin = input("De que aminoacido quieres buscar el porcentaje?: ")

# Funcion con la que se saca el porcentaje
def porcentajeamin(sec, amin):
    porcentaje = round(((sec.upper().count(amin.upper())) / len(sec)) * 100)
    return(porcentaje)


assert porcentajeamin("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert porcentajeamin("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert porcentajeamin("msrslllrfllfllllpplp", "L") == 50
assert porcentajeamin("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

#porcentajeamin(sec, amin)
