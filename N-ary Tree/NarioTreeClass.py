from NarioTreeNodeClass import NarioTreeNodeClass
import json
import jsonpickle

class NarioTreeClass:
    ''' Class N-ary Search Tree Class which is the representation of ADT 
        structure where nodes can have no more than N nodes 
        and N-1 elements.
        Args:
            Orden:  The value will define the number of elements 
                    and children the tree will manage. 
            elemento:   First Node's data value ###put it in the 
                        imported class.
        Attributes:
            Raiz:   It creates the link to the first structure node 
                    in the N-ary Search Tree. It defaults to None.
            Orden:  The value will define the number of elements 
                    and children the tree will manage.   
    '''
    def __init__(self, orden = None):
        ''' Inits a instance of N-ary Search Tree with default values 
            in their attirbutes
        '''
        self.__raiz = None
        self.__orden = orden

    def getOrden(self):
        ''' Getter method for returning the root node of AVLTree '''
        return self.__orden
    
    def setOrden(self, orden):
        ''' Setter method for setting the  node of AVLTree 
            Args:
                link(Node)
        '''
        self.__orden = orden
    
    def getRaiz(self):
        ''' Getter method for returning the N-ary Search Tree's 
            root node
            Return:
                The reference to the root node 
        '''
        return self.__raiz

    def setRaiz(self, raiz):
        ''' Setter method for setting the N-ary Search Tree's root 
            node of AVLTree 
            Args:
                raiz(Node)
        '''
        self.__raiz = raiz

    def esNodoVacio(self, current):
        ''' Check if whether the node is empty or not
            Return:
                True: The node is empty
                False: The node has at least on element
        '''
        return current == None
    
    def esArbolVacio(self):
        ''' Check the whole tree if whether is empty or not
            Return:
                True: The tree is empty
                False: The node has at least on element
        '''
        return self.esNodoVacio(self.__raiz)

    def esNodoHoja(self, current):
        ''' Check a node if whether is a leaf or not
            Args:
                current: the current node to check
            Return:
                True: The node is a leaf
                False:  The node has at least one child
        '''
        for i in range(0, self.__orden -1):
            if( current.esHijoVacio(i) == True ):
                return True
        return False

    def existeDatoEnNodo(self, current, elemento):
        ''' Verify a element if it's already within a node or not
            Args:
                current(Node): the current node where the element has 
                               to be verified
                elemento(object): the element to be verified
            Return:
                True: The element already exists within current node
                False: The element doesn't exists within current node
        '''
        i = 0
        while( (i < self.__orden-1) and (current.EsElementoVacio(i) == False) ):
            if( elemento == current.getElemento(i)):
                return True
            i += 1
        return False
    
    def enQueHijoVa(self, current, elemento):
        ''' Method to determine in which position a child node 
            will be created.
            Args:
                current(Node): The current node it's being analyzed
                element(object): The element is being attempted to 
                                 insert
            Return:
                i: the position where a child node has to be created
                -1: the element already exists in the node
        '''
        cantidadNodosOcupados = current.getNroElementosOcupados()
        i = 0
        while( i < cantidadNodosOcupados ):
            if( elemento == current.getElemento(i)):
                return -1
            if( elemento < current.getElemento(i)):
                return i
            i += 1
        return i
    
    def insertar(self, elemento):
        ''' Method to insert an element in its correct position within
            the N-ary Search Tree
            Args:
                elemento(object): the value its being attempted 
                                  to insert
        '''
        if( self.esArbolVacio()):
            self.setRaiz(NarioTreeNodeClass(self.__orden, elemento))
            return 
        current = self.getRaiz() #Makes a copy of the original root
        while( self.esNodoVacio(current) == False):
            if(self.esNodoHoja(current)):
                if( current.EstaNodoLleno() ):
                    posicionHijo = self.enQueHijoVa(current, elemento)
                    if (posicionHijo != -1 ):
                        nuevoNodo = NarioTreeNodeClass(self.__orden, elemento)
                        current.setHijo(posicionHijo, nuevoNodo)
                        return
                    else:
                        return
                elif (self.existeDatoEnNodo(current, elemento) == False):
                    current.insertarElemento(elemento)
                else:
                    return
            else:
                posicionHijo = self.enQueHijoVa(current, elemento)
                if(posicionHijo == -1):
                    return
                if( current.esHijoVacio(posicionHijo)):
                    nuevoNodo = NarioTreeNodeClass(self.__orden, elemento)
                    current.setHijo(posicionHijo, nuevoNodo)
                    return
                current = current.getHijo(posicionHijo)
        
    '''def showAsJson(self):
        raiz = self.getRaiz()
        json_list = json.JSONEncoder(raiz)
        print(json_list)
    '''
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=3)



def main():
    print("Test of the N-ary Tree")
    Kario = NarioTreeClass(5)
    Kario.insertar(23)
    Kario.insertar(37)
    Kario.insertar(85)
    Kario.insertar(49)
    Kario.insertar(22)
    Kario.insertar(36)
    Kario.insertar(83)
    Kario.insertar(42)
    Kario.insertar(7)
    Kario.insertar(13)
    Kario.insertar(43)
    Kario.insertar(75)
    Kario.insertar(24)
    Kario.insertar(53)
    Kario.insertar(82)
    Kario.insertar(30)
    Kario.insertar(34)
    Kario.insertar(60)
    Kario.insertar(22)
    #json_data = json.dumps(Kario.getRaiz(), default=lambda o: o.__dict__, 
    #        sort_keys=True, indent=3)
    json_data = Kario
    #Kario.showAsJson()
    #json_data = Kario.toJSON()
    #i = 0
    '''
        while (i < Kario.getOrden()-1):
        json_data = Kario.getRaiz().getElemento(i)
        json.dumps(json_data, indent=3)
        print(json_data)
        i +=1
    '''
#    print(json_data) 
    print(json_data)
    #json_data = jsonpickle.encode(Kario, indent=3)
    #print(json_data)

    with open('data7.json', 'w') as f:
        json.dump(json_data, f, indent=3, default=lambda o: o.__dict__)
    print(0)

if __name__ == "__main__":
    main()