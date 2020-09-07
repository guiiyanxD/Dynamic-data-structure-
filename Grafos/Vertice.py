
class Vertice:
    def __init__(self, valor):
        self.__valor = valor
        self.__arista_parte = []
        self.__arista_llega = []
    
    def getValor(self):
        return self.__valor
    
    def setValor(self, valor):
        self.__valor = valor

    def setPartida(self, arista):
        self.__arista_parte.append(arista)

    def setLlegada(self, arista):
        self.__arista_llega.append(arista)

    def getCantidadPartidas(self):
        return len(self.__arista_parte)
    
    def getCantidadLlegadas(self):
        return len(self.__arista_llega)


    #def getPartida(self, posicion):
    #    for i in self.__arista_parte:
    #        if (i == posicion):
    #            return i
    #        else:
    #            print("No es punto de ")


