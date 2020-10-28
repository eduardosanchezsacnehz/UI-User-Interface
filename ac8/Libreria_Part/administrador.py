from particula import Particula

class Administrador:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )


#l01 = Particula(id="9083427", origen_x="34", origen_y="102", destino_x="105", destino_y="241", velocidad="123", red="65",  green="232", blue="250", distancia="")
#l02 = Particula(id="8834432", origen_x="43", origen_y="12", destino_x="210", destino_y="20", velocidad="43", red="125",  green="221", blue="210", distancia="")
#Administrador = Administrador()
#Administrador.agregar_final(l01)
#Administrador.agregar_inicio(l02)
#Administrador.agregar_inicio(l01)
#Administrador.mostar()