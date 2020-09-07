
class Vertice:
    ''' La clase vertice representa el tipo de dato abstracto de un
        vertice que podria ser capaz de almacenar objetos dentro de el
        Args:
            Valor(Objeto): La informacion(objeto) del vertice. Por 
                           defecto el valor es None
            Arista_parte(lista): Lista de vertices a los que un vertice
                                 especifico esta dirigido
            Arista_Llega(lista): Lista de vertices que llegan hacia un
                                 vertice en especifico
    '''
    def __init__(self, valor=None):
        ''' Inicializa una instancia de un vertice con sus valores
            por defecto
        '''
        self.__valor = None
        self.__arista_parte = []
        self.__arista_llega = []
    
    def getValor(self):
        ''' Metodo getter para obtener el valor(informacion u objeto)
            de un vertice especifico.
        '''
        return self.__valor
    
    def setValor(self, valor):
        ''' Metodo setter para establecer el valor(informacion 
            u objeto) de un vertice.
            Args:
                valor(objeto): La informacion que el vertice contendra
        '''
        self.__valor = valor

    def setPartida(self, arista):
        ''' Metodo setter que agrega una referencia, de otro vertice a
            donde uno en especifico se dirige, a la lista.
            Args:
                arista: la referencia del vertice al cual un vertice
                        determinado esta dirigido
        '''
        self.__arista_parte.append(arista)

    def setLlegada(self, arista):
        ''' Metodo setter que agrega una referencia, de otro vertice el 
            cual esta dirigido a un vertice determinado, a la lista.
            Args:
                arista: la referencia de un vertice que se dirige a un vertice
                        determinado 
        '''
        self.__arista_llega.append(arista)

    def getCantidadPartidas(self):
        ''' Metodo getter que retorna la longitud de la lista 
            arista_parte
        '''
        return len(self.__arista_parte)
    
    def getCantidadLlegadas(self):
        ''' Metodo getter que retorna la longitud de la lista 
            arista_llega
        '''
        return len(self.__arista_llega)


    #def getPartida(self, posicion):
    #    for i in self.__arista_parte:
    #        if (i == posicion):
    #            return i
    #        else:
    #            print("No es punto de ")


