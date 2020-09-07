
class Arista:
    ''' La clase arista representa el tipo de dato abstracto el cual
        es un puente entre dos vertices, es decir, almacena la 
        referencia de los vértices que estan situados en cada una de
        las puntas de la arista.
        Args:
            Origen: La referencia del vértice desde donde nace la arista. 
                    Su valor por defecto es None
            Destino: La referencia del vértice hacia donde la arista 
                     está dirigida. Su valor por defecto es None
    '''

    def __init__(self, origen = None, destino = None):
        ''' Inicializa una instancia de una arista con sus valores
            por defecto
        '''
        self.__origen = origen
        self.__destino = destino
    
    def setOrigen(self, origen):
        ''' Método setter para establecer la referencia del vértice de
            origen de una arista.
            Args:
                origen(vertice): referencia del vertice desde donde la arista nace.
        '''
        self.__origen = origen
    
    def getOrigen(self):
        ''' Método getter para obtener la referencia del vertice de 
            origen de una arista 
        '''
        return self.__origen

    def setDestino(self, destino):
        ''' Método setter para establecer la referencia del vértice de
            destino de una arista.
            Args:
                origen(vertice): referencia del vertice hacia donde la arista esta dirigida.
        '''
        self.__destino = destino
    
    def getDestino(self):
        ''' Método getter para obtener la referencia del vertice de 
            destino de una arista 
        '''
        return self.__destino