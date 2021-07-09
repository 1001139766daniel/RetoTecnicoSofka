import random

class Carro():
    def __init__(self, numero):
        self.numero = numero

class Carril():
    def __init__(self, nCarril, dRecorrida):
        self.nCarril = nCarril
        self.dRecorrida = dRecorrida

class Jugador():
    def __init__(self, carro, nombre, carril):
        self.carro = carro
        self.nombre = nombre
        self.carril = carril

class Pista():
    def __init__(self, nCarros, distancia, jugadores):
        self.nCarros = nCarros
        self.distancia = distancia
        self.jugadores = jugadores

class Juego():
    def __init__(self, pista):
        self.pista = pista


    def partida(self):
        podio = []
        self.pista.distancia = self.pista.distancia*1000

        while len(podio)!=3:
            for jugador in self.pista.jugadores:
                dado = random.randint(1, 6)
                vMetro = dado*100
                vMetro = float(vMetro)
                vKilometros = vMetro/1000
                vKilometros = float(vKilometros)
                jugador.carril.dRecorrida = jugador.carril.dRecorrida + vKilometros
                jugador.carril.dRecorrida = f'{jugador.carril.dRecorrida:.1f}'
                print("El jugador #", jugador.carro.numero, " de nombre: ", jugador.nombre, " saco ", dado, " en el dado y suma: ", vMetro, " metros, y ha recorrido un total de: ", jugador.carril.dRecorrida, " metros recorridos \n")
                jugador.carril.dRecorrida = float(jugador.carril.dRecorrida)
                if jugador.carril.dRecorrida >= self.pista.distancia:
                    if len(podio) == 0:
                        podio.append(jugador)
                    else:
                        cond = "false"
                        for ganadores in podio:
                            if jugador.nombre in ganadores.nombre:
                                cond = "true"
                                break
                        if cond=="false":
                           podio.append(jugador)
        aux=0
        print("\n ******************************* GANADORES *******************************")
        for ganadores in podio:
            aux=aux+1
            print("El puesto ", aux, " es para el jugador: ", ganadores.nombre)
        return "Terminé"

    
    





