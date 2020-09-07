
class Arista:

    def __init__(self, origen = None, destino = None):
        self.__origen = origen
        self.__destino = destino
    
    def setOrigen(self, origen):
        self.__origen = origen
    
    def getOrigen(self):
        return self.__origen

    def setDestino(self, destino):
        self.__destino = destino
    
    def getDestino(self):
        return self.__destino