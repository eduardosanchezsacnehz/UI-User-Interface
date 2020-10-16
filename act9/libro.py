from algoritmos import distancia_ecualidiana

class Particula:
    def __init__(self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red=0, green=0, blue=0, distancia=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_ecualidiana(origen_x=0, origen_y=0, destino_x=0, destino_y=0)

    def __str__(self):
        return (
            'id: ' + str(self.__id) + '\n' +
            'origen_x: ' + str(self.__origen_x) + '\n' +
            'origen_y: ' + str(self.__origen_y) + '\n' +
            'destino_x: ' + str(self.__destino_x) + '\n' +
            'destino_y: ' + str(self.__destino_y) + '\n' +
            'velocidad: ' + str(self.__velocidad) + '\n' +
            'red: ' + str(self.__red) + '\n' +
            'green: ' + str(self.__green) + '\n' +
            'blue: ' + str(self.__blue) + '\n' +
            'distncia: ' + str(self.__distancia) + '\n' 
        )

#    l01 = Particula(id=1234567890, origen_x=12, origen_y=12, destino_x=0, destino_y=0, velocidad=10, red=0, green=0, blue=0, distancia=100.15)
#    print(l01)
#    l02 = Particula("Python", "Guiado")
#    print(l02)