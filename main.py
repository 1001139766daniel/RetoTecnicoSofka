import objects
import DataBase

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
ganadores = juego.partida()
print("****************************************************** FIN del Juego **************************************\n")
createDataBase = int(input("¿Si desea crear la base de datos ingrese 1? (Si ya está creada e ingresa 1 genera error) \n"))
if createDataBase==1:
    DataBase.createDataBase()

cont=0
for ganador in ganadores:
    cont=cont+1
    if cont==1:
        DataBase.insertResults(ganador.nombre, "1", "0", "0")
    if cont==2:
        DataBase.insertResults(ganador.nombre, "0", "1", "0")
    if cont==3:
        DataBase.insertResults(ganador.nombre, "0", "0", "1")
    DataBase.consulta(ganador.nombre)
