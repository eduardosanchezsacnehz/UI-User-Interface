from libro import Particula

class Libreria:
    def __init__(self):
        self.__libros = []

    def agregar_final(self, libro:Particula):
        self.__libros.append(libro)

    def agregar_inicio(self, libro:Particula):
        self.__libros.insert(0, libro)

    def mostrar(self):
        for libro in self.__libros:
            print(libro)

l01 = Particula(id=1234567890, origen_x=12, origen_y=12, destino_x=0, destino_y=0, velocidad=10, red=0, green=0, blue=0, distancia=100.15)
l02 = Particula("Python", "Guiado")
libreria = Libreria()
libreria.agregar_final(l01)
libreria.agregar_inicio(l02)
libreria.mostrar()
