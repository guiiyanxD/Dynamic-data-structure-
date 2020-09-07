from Vertice import Vertice
from Arista import Arista
import json

class Grafo:
    def __init__(self):
        self.__Vertices = []
        self.__Aristas = []
        #self.__cantidadV = 0
        #self.__cantidadA = 0
    
    def insertarV(self, valor):
        self.__Vertices.append( Vertice(valor) )
        #self.__cantidadV += 1

    def buscarV(self, valor):
        for i in range(0, (len(self.__Vertices))):
            if valor == self.__Vertices[i].getValor():
                return self.__Vertices[i]
        return None
    
    def buscarA(self, origen, destino):
        for i in range(0, len(self.__Aristas)):
            raiz = i.getOrigen()
            fin = i.getDestino()
            if ( raiz.getValor() == origen.getValor() and fin.getValor() == destino.getValor() ):
                return i 
            else:
                return None

    def insertarA(self, origen, destino):
        origen_aux = self.buscarV(origen)
        destino_aux = self.buscarV(destino)
        if( (origen_aux != None) and (destino_aux != None) ):
            self.__Aristas.append(Arista(origen_aux, destino_aux))
        #self.__cantidadA += 1

    def ContarParticipaciones(self):
        self.ContarPartidas()
        self.ContarLlegadas()

    def ContarPartidas(self):
        for i in range(0, len(self.__Vertices)):
            vertice_aux = self.__Vertices[i].getValor()
            for j in range(0, len(self.__Aristas)):
                origen_aux = self.__Aristas[j].getOrigen().getValor()
                destino_aux = self.__Aristas[j].getDestino().getValor()
                if(vertice_aux == origen_aux):
                    self.__Vertices[i].setPartida(destino_aux)

    def ContarLlegadas(self):
        for i in range(0, len(self.__Vertices)):
            vertice_aux = self.__Vertices[i].getValor()
            for j in range(0, len(self.__Aristas)):
                origen_aux = self.__Aristas[j].getOrigen().getValor()
                destino_aux = self.__Aristas[j].getDestino().getValor()
                if(vertice_aux == destino_aux):
                    self.__Vertices[i].setLlegada(origen_aux)


    def grafoVacio(self):
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