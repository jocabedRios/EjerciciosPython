# Realizar el juego de Piedra, Papel o Tijera con dos jugadores
print("Piedra, Papel o Tijera")
jugador1 = input("Jugador1: ")
jugador2 = input("Jugador2: ")
opciones = ["Piedra", "Papel", "Tijera"]

if jugador1 not in opciones or jugador1 not in opciones:
    print("Entradas incorrectas :c")
elif jugador1==jugador2:
    print("Empate!")
elif jugador1 == "Piedra":
    if jugador2 == "Papel":
        print("Jugador2 wins!!!")
    else:
        print("Jugador1 wins!!!")
elif jugador1 == "Papel":
    if jugador2 == "Tijera":
        print("Jugador2 wins!!!")
    else:
        print("Jugador1 wins!!!")
else: 
    if jugador2 == "Piedra":
        print("Jugador2 wins!!!")
    else:
        print("Jugador1 wins!!!")
