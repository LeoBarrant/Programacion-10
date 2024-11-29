import random

class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def validarNumero(self, numero):
        if numero > self.numero_secreto:
            return "El número es menor."
        elif numero < self.numero_secreto:
            return "El número es mayor."
        else:
            return "¡Correcto! Has adivinado el número."

    def registrarIntento(self):
        self.intentos += 1

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contador = []

    def registrarPartida(self, intentos, gano):
        self.contador.append({
            "intentos": intentos,
            "gano": gano
        })

    def mostrarEstadisticas(self):
        total_partidas = len(self.contador)
        partidas_ganadas = sum(1 for partida in self.contador if partida["gano"])
        porcentaje_aciertos = (partidas_ganadas / total_partidas) * 100 if total_partidas > 0 else 0
        return f"Partidas jugadas: {total_partidas}, Partidas ganadas: {partidas_ganadas}, Porcentaje de aciertos: {porcentaje_aciertos:.2f}%"

def menu():
    print("1. Comenzar una nueva partida")
    print("2. Ver las estadísticas del jugador")
    print("3. Salir del juego")
    opcion = input("Elige una opción: ")
    return opcion

def cargar_estadisticas(nombre):
    contador = []
    try:
        with open("estadisticas.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == nombre:
                    contador.append((int(data[1]), data[2] == 'True'))
    except FileNotFoundError:
        pass
    return contador

def guardar_estadisticas(nombre, contador):
    with open("estadisticas.txt", "a") as file:
        for partida in contador:
            file.write(f"{nombre},{partida['intentos']},{partida['gano']}\n")

def juego():
    nombre = input("Introduce tu nombre: ")
    jugador = Jugador(nombre)

    historial_cargado = cargar_estadisticas(nombre)
    for intentos, gano in historial_cargado:
        jugador.contador.append({"intentos": intentos, "gano": gano})

    while True:
        opcion = menu()
        if opcion == "1":
            juego = JuegoAdivinanza()
            while True:
                numero = int(input("Adivina el número (entre 1 y 100): "))
                resultado = juego.validarNumero(numero)
                juego.registrarIntento()
                print(resultado)
                if resultado == "¡Correcto! Has adivinado el número.":
                    jugador.registrarPartida(juego.intentos, True)
                    break
        elif opcion == "2":
            print(jugador.mostrarEstadisticas())
        elif opcion == "3":
            guardar_estadisticas(nombre, jugador.contador)
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Por favor, elige de nuevo.")

if __name__ == "__main__":
    juego()
