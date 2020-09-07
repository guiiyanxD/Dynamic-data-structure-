from Vertice import Vertice
from Arista import Arista
import json

class Grafo:
    ''' Clase grafo que representa el tipo de dato abstracto el cual es
        una coleccion de vertices y aristas que se conectan entre si 
        para formar un grafo.
        Args:
            Vertices(lista): Lista de referencias que almacena todos
                             los vertices que formaran un nodo.
            Aristas(lista): Lista de referencias que almacena todas las
                            aristas que formaran un nodo.                             
    '''
    def __init__(self):
        ''' Inicializa una instancia de un grafo '''
        self.__Vertices = []
        self.__Aristas = []
        #self.__cantidadV = 0
        #self.__cantidadA = 0
    
    def insertarV(self, valor):
        ''' Metodo para insertar un vertice dentro de la lista de
            Vertices
            Args:
                valor(objeto): el valor(informacion) contendra el vertice
        '''
        self.__Vertices.append( Vertice(valor) )
        #self.__cantidadV += 1

    def buscarV(self, valor):
        ''' Metodo para buscar el valor de un vertice especifico dentro
            de la lista de Vertices
            Args:
                valor(objeto): El valor del vertice que sera buscado.
            Return:
                return: referencia del vertice que esta siendo buscado
                None: el vertice buscado no existe. 
        '''
        for i in range(0, (len(self.__Vertices))):
            if valor == self.__Vertices[i].getValor():
                return self.__Vertices[i]
        return None
    
    def buscarA(self, origen, destino):
        ''' Metodo para buscar una arista especifica dentro de la lista
            de los Aristas
            Args:
                origen(objeto): El valor del vertice de origen que sera
                                buscado dentro de la lista de Aristas.
                destino(objeto): El valor del vertice de llegada que sera
                                 buscado dentro de la lista de Aristas.
            Return:
                i: referencia de la arista que esta siendo buscada
                None: la arista buscada no existe.
        '''
        for i in range(0, len(self.__Aristas)):
            raiz = i.getOrigen()
            fin = i.getDestino()
            if ( raiz.getValor() == origen.getValor() and fin.getValor() == destino.getValor() ):
                return i 
            else:
                return None

    def insertarA(self, origen, destino):
        ''' Metodo para insertar una arista dentro de la lista de
            Aristas
            Args:
                origen(objeto): el valor del vertice de origen. 
                destino(objeto): el valor del vertice de destino. 
        '''
        origen_aux = self.buscarV(origen)
        destino_aux = self.buscarV(destino)
        if( (origen_aux != None) and (destino_aux != None) ):
            self.__Aristas.append(Arista(origen_aux, destino_aux))

    def ContarParticipaciones(self):
        ''' Metodo que establece las participaciones de cada uno de los
            vertices
        '''
        self.ContarPartidas()
        self.ContarLlegadas()

    def ContarPartidas(self):
        ''' Metodo que cuenta y almacena las referencias de los
            vertices, a los cuales un vertice en especifico esta
            dirigido, dentro de la lista Arista_parte
        '''
        for i in range(0, len(self.__Vertices)):
            vertice_aux = self.__Vertices[i].getValor()
            for j in range(0, len(self.__Aristas)):
                origen_aux = self.__Aristas[j].getOrigen().getValor()
                destino_aux = self.__Aristas[j].getDestino().getValor()
                if(vertice_aux == origen_aux):
                    self.__Vertices[i].setPartida(destino_aux)

    def ContarLlegadas(self):
        ''' Metodo que cuenta y almacena las referencias de los
            vertices, a los cuales un vertice en especifico se dirige,
            dentro de la lista Arista_llega
        '''
        for i in range(0, len(self.__Vertices)):
            vertice_aux = self.__Vertices[i].getValor()
            for j in range(0, len(self.__Aristas)):
                origen_aux = self.__Aristas[j].getOrigen().getValor()
                destino_aux = self.__Aristas[j].getDestino().getValor()
                if(vertice_aux == destino_aux):
                    self.__Vertices[i].setLlegada(origen_aux)


    def grafoVacio(self):
        ''' Metodo que define si el grafo esta vacio o no.
            Return:
                True: El grafo esta vacio
                False: El grafo contiene al menos un vertice.
        '''
        if ( len(self.__Vertices) == 0):
            return True
        else:
            return False 
    
    def __str__(self):
        if (self.grafoVacio()):
            strV = "Vertices: { }"
            strA = "Aristas: { }"
            final = strV + '\n' + strA
            return final    
        else:
            strV = "Vertices: { "
            strA = " Aristas: { "
            for i in range(0, (len(self.__Vertices))):
                aux = str(self.__Vertices[i].getValor())
                strV = strV + aux 
                if i == len(self.__Vertices)-1:
                    strV = strV + "}"
                else:
                    strV = strV + ", "

            for i in range(0, (len(self.__Aristas))):
                aux = "[ " + str(self.__Aristas[i].getOrigen().getValor()) + " , "+str(self.__Aristas[i].getDestino().getValor()) + " ]" 
                strA = strA + aux
                if i == len(self.__Aristas)-1:
                    strA = strA + "}"
                else:
                    strA = strA + ", "
            final = strV + '\n' + strA
            return final

def main():
    grafo = Grafo()
    grafo.insertarV(80)
    grafo.insertarV(30)
    grafo.insertarV(25)
    grafo.insertarV(10)
    grafo.insertarV(200)
    grafo.insertarV(1)
    grafo.insertarA(80,200)
    grafo.insertarA(30,10)
    grafo.insertarA(25,80)
    grafo.insertarA(80,1)
    grafo.insertarA(200,30)
    grafo.ContarParticipaciones()
    print(grafo)
    json_data = grafo
    with open('data3.json', 'w') as f:
        json.dump(json_data, f, indent=3, default=lambda o: o.__dict__)

    

if __name__ == "__main__":
    main()