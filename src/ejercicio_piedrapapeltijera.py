'''
NAME
	ejercicio_piedrapapeltijera.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Piedra, papel y tijeras contra computadora
        
CATEGORY
	Juego
    
USAGE
    python ejercicio_piedrapapeltijera.py
'''


import random

# Pedimos al usuario su input, se usa lower para que se 
# pueda leer la respuesta aunque este en mayusculas
usuario = input("Elige; piedra, papel o tijeras:\n").lower()

# La computadora hace su eleccion
opciones = ["piedra","papel","tijeras"]
num_aleato = random.randint(0, 2)
computadora = opciones[num_aleato]

if usuario not in opciones:
    print("Error! Opción no valida vuelve a intentarlo")
    exit()

print("La computadora eligio: {}".format(computadora))
print("El usuario eligio: {}".format(usuario))


# Empate, usuario es igual a computadora
if(usuario == computadora):
    print("Empate")
    
else:

    # Se checan las opciones si el usuario eligio tijeras
    if(usuario == "tijeras"):
        if(computadora == "piedra"):
            print("Usuario pierde")
        else:
            print("Usuario gana")

    # Se checan las opciones si el usuario eligio piedra
    if(usuario == "piedra"):
        if(computadora == "papel"):
            print("Usuario pierde")
        else:
            print("Usuario gana")

    # Se checan las opciones si el usuario eligio piedra
    if(usuario == "papel"):
        if(computadora == "tijeras"):
            print("Usuario pierde")
        else:
            print("Usuario gana")
