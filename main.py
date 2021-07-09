import objects

nJugadores = int(input("¿Cuantos jugadores habrán? \n"))
distancia = float(input("¿Cuantos kilometros tendrá la pista? \n"))

listJugadores = []
i = 0

while nJugadores != i:
    i=i+1
    carros = objects.Carro(i)
    carril = objects.Carril(i, 0)
    print("Ingrese el nombre del jugador: ")
    nombreJugador = str(input())
    jugadores = objects.Jugador(carros, nombreJugador, carril)
    listJugadores.append(jugadores)

#Mostrar tabla de jugadores
print("Se tienen los siguientes jugadores: ")
for jugador in listJugadores:
    print(jugador.nombre, "Tiene  el auto #", jugador.carro.numero, " y correrá por el carril #", jugador.carro.numero)

#Empezar juego
pista = objects.Pista(nJugadores, distancia, listJugadores)

juego = objects.Juego(pista)
print("****************************************************** Inicio del Juego ******************************************************")
juego.partida()





