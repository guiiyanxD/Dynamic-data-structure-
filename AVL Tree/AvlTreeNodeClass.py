'''============================================================
    Author: Williams Wilman Alvarez Zabala
    ===========================================================
'''

class Nodo:
    ''' Class Node which is made for representing ADT structure contains
        data and links to connect to other nodes.
        Args:
            daata(obj): First Node's data value
        Attributes:
            data(obj): First Node's data value
            hijoIzq: A link that points to its left child node
            hijoDer: A link that ponits to its right child node
            level(int): An integer specifies the nodes's level within 
                        the binary tree. Defaults to zero(0)
    '''
    def __init__(self, dato):
        ''' Inits class Nodo with default values in their attributes '''
        self.__data = dato
        self.__HijoIzquierdo = None
        self.__HijoDerecho = None
        self.__level = 0
        self.__parent = None


#. Methods getter and setter for getting and setting the parent
    def setParent(self, parent):
        ''' Setter method for setting the parent node of the 
        data structure
        '''
        self.__parent = parent
    def getParent(self):
        ''' Getter method for returning the parent node of the 
            data structure 
        '''
        return self.__parent

    #. Methods getter and setter for getting and setting the left node        
    def getHijoIzquierdo(self):
        ''' Getter method for returning the left child node of the 
            data structure 
        '''
        return self.__HijoIzquierdo

    def setHijoIzquierdo(self, HI):
        ''' Setter method for setting the left child node of the 
            data structure
        '''
        self.__HijoIzquierdo = HI
            
    #. Methods getter and setter for getting and setting the right node  
    def getHijoDerecho(self):
        ''' Getter method for returning the right child node of the 
            data structure 
        '''
        return self.__HijoDerecho
    
    def setHijoDerecho(self, HD):
        ''' Setter method for setting the left child node of the 
            data structure
        '''
        self.__HijoDerecho = HD

    #. Methods getter and setter for getting and setting data in a node
    def getData(self):
        ''' Getter method for getting the data from a node of the 
            data structure
        '''
        return self.__data
    
    def setData(self, dato):
        ''' Setter method for Setting the data from a node of the 
            data structure
        '''
        self.__data = dato

    #. Methods getter and setter for getting and setting node's level
    def setLevel(self, level):
        ''' Setter method for setting the level from a node of the 
            data structure
        '''
        self.__level = level

    def getLevel(self):
        ''' Getter method for getting the level from a node of the 
            data structure
        '''
        return self.__level