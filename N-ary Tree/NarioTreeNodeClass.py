import queue as queue

class NarioTreeNodeClass:
    def __init__(self, orden, elemento = None):
        ''' Class N-ary Search Tree Node Class which is a list 
            representation of ADT Structure Node where it's possible
            to store N-1 elements.
            Args:
                orden:  The value will define the number of elements 
                        and children the tree will manage. 
                elemento: First Node's data value
            Attributes:
            Hijos[](list): A list where the child nodes will be stored.
            Elementos[](list): A list where the node's elements 
                               will be stored
            Orden(int):  The value will define the number of elements
                         and children the tree will manage.   
        '''
        self.__Hijos = []
        self.__Elementos = []
        self.__orden = orden

        
        for i in range(0, self.__orden):
            self.__Hijos.append(None)

            if(i < (self.__orden-1)):
                self.__Elementos.append(None)
        self.__Elementos[0] = elemento
    
    def getElemento(self, posicion):
        ''' Getter method for getting a specific element in the list by
            passing the position as argument
            Args:
                posicion(int): The position of the element 
                               to be returned
            Return:
                The element in the specified position
        '''
        return self.__Elementos[posicion]

    def setElemento(self, posicion, dato):
        ''' Setter method for setting an element in a specific position
            Args:
                posicion(int): The position of the element 
                               to be set
                dato(object): The element its being set
        '''
        self.__Elementos[posicion] = dato
    
    def getHijo(self, posicion):
        ''' Getter method for getting a specific child list by
            passing the position as argument
            Args:
                posicion(int): The position of the child list 
                               to be returned
            Return:
                The child list in the specified position
        '''
        return self.__Hijos[posicion]

    def setHijo(self, posicion, hijo):
        ''' Setter method for setting a child list in a specific
            position
            Args:
                posicion(int): The position of the child list 
                               to be set
                hijo(list): The child list it's being set
        '''
        self.__Hijos[posicion] = hijo

    def getNroElementosVacios(self):
        ''' Check how many empty slots there are in the elements list
            Return:
                cantidad(int): the quantity of empty slots there
                               are in the elements list
        '''
        cantidad = i = 0
        while(i < self.__orden):
            if(self.__Elementos[i] == None):
                cantidad += 1
        return cantidad

    def getNroElementosOcupados(self):
        ''' Check how many not empty slots there are in the elements list
            Return:
                cantidad(int): the quantity of not empty slots there
                               are in the elements list
        '''
        cantidad = i = 0
        while(i < self.__orden -1 ):
            if(self.__Elementos[i] != None):
                cantidad += 1
            i += 1
        return cantidad

    def getNroHijosVacios(self):
        ''' Check how many empty slots there are in the child list
            Return:
            cantidad(int): The quantity of empty slots there
                           are int the child list
        '''
        cantidad = i = 0
        while(i <= self.__Hijos.__len__()):
            if(self.__Hijos[i] == None):
                cantidad += 1
        return cantidad

    def getNroHijosOcupados(self):
        ''' Check how many not empty slots there are in the child list
            Return:
                cantidad(int): the quantity of not empty slots there
                               are in the child list
        '''
        cantidad = i = 0
        while(i < self.__Hijos.__len__()):
            if(self.__Hijos[i] != None):
                cantidad += 1 
            i += 1
        return cantidad
    
    def EsElementoVacio(self, posicion):
        ''' Verify a specific slot if whether is empty or not
            in the element list
            Args:
                position(int): position to be checked.
            Return:
                True: the position is empty
                False: The position os not empty
        '''
        if (self.__Elementos[posicion] == None):
            return True
        else: 
            return False
    
    def esHijoVacio(self, posicion):
        ''' Verify a specific slot if whether is empty or not
            in the child list
            Args:
                position(int): position to be checked.
            Return:
                True: the position is empty
                False: The position is not empty
        '''
        return self.__Hijos[posicion] == None

    def getUltimoElementoOcupado(self):
        ''' Getter method for getting the index of the last slot not 
            empty in the element list
            Return:
                The position of the last slot not empty 
                in the element list
        '''
        i = 0
        while(i < self.__orden - 1):
            if( self.EsElementoVacio(i) ):
                return i #self.__Elementos[i] 
            i += 1
        return 0
    
    def EstaNodoLleno(self):
        ''' Verify if a node has all the slots not empty in its list
            Return:
                True: the entire node it's not empty
        '''
        if (self.getNroElementosOcupados() == self.__orden-1):
            return True
        else:
            return False

    def insertarElemento(self, elemento):
        ''' Method to insert an element in its correct position within
            the list
            Args:
                elemento(object): the value its being attempted 
                                  to insert
        '''
        posicion = self.getUltimoElementoOcupado()
        while (posicion > 0):
            if (elemento < self.__Elementos[posicion-1]):
                self.__Elementos[posicion] = self.__Elementos[posicion -1 ]
            else:

                self.__Elementos[posicion] = elemento
                return
            posicion -= 1 
        self.__Elementos[0] = elemento 
      