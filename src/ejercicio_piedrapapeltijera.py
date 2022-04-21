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
'''


import random

jugar_denuevo = "si"

while jugar_denuevo.lower() == "si":

    # Pedimos al usuario su input, se usa lower para que se pueda leer la respuesta aunque este en mayusculas
    usuario = input("Elige; piedra, papel o tijeras: ").lower()

    # La computadora tiene su opcion
    num_aleato = random.randint(1, 3)

    if(num_aleato == 1):
        computadora = "piedra"

    if(num_aleato == 2):
        computadora = "papel"

    if(num_aleato == 3):
        computadora = "tijeras"

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
    # Se le pregunta al usuario si quiere jugar denuevo
    jugar_denuevo = input("Quieres jugar denuevo? (si/no): ")
