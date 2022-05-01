'''
NAME
	ejercicio_piedrapapeltijera.py
    
VERSION
    1.1
    
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

opciones = ["piedra", "papel", "tijeras"]

while jugar_denuevo.lower() == "si":

    # Pedimos al usuario su input, se usa lower para que se pueda leer la respuesta aunque este en mayusculas
    usuario = input("Elige; piedra, papel o tijeras: ").lower()
    if(usuario in opciones):

        # La computadora tiene su opcion
        computadora = random.choice(opciones)
        print(f"Computadora elige {computadora}")

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

    else:
        print("Esa opcion no esta disponible")
    # Se le pregunta al usuario si quiere jugar denuevo
    jugar_denuevo = input("Quieres jugar denuevo? (si/no): ")
