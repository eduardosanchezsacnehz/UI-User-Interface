from libro import Particula

class Administrador:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, libro:Particula):
        self.__particulas.append(libro)

    def agregar_inicio(self, libro:Particula):
        self.__particulas.insert(0, libro)

    def mostar(self):
        for libro in self.__particulas:
            print(libro)


l01 = Particula(id="908765", origen_x="12", origen_y="50", destino_x="40", destino_y="11", velocidad="90", red="120",  green="22", blue="75", distancia="")
l02 = Particula(id="987654", origen_x="9", origen_y="10", destino_x="11", destino_y="12", velocidad="0", red="132",  green="20", blue="30", distancia="0")
Administrador = Administrador()
Administrador.agregar_final(l01)
Administrador.agregar_inicio(l02)
Administrador.agregar_inicio(l01)
Administrador.mostar()