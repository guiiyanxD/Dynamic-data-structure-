'''============================================================
    Author: Williams Wilman Alvarez Zabala
    ===========================================================
'''

from Node import Nodo

class ArbolBinario:
    ''' Class ArbolAVL which represents AVLTree ADT is self balanging
        tree that cointains a collection of nodes which will be ordered
        by standard rules.
        Attributes:
            Raiz: It creates the link to the first node in an AVLTree.
                  It defaults to None.
            Rango: It's the balance factor. Defaults 1.
    '''
    
    def __init__(self):
        ''' Inits a instance of AvlTree with default values in their
             attirbutes
        '''
        self.__raiz = None
        self.__Rango = 1
        
    def setRoot(self,link):
        ''' Setter method for setting the root node of AVLTree 
            Args:
                link(Node)
        '''
        self.raiz = link

    def getRoot(self):
        ''' Getter method for returning the root node of AVLTree '''
        return self.__raiz

    def alturaRecursivo(self, nodo):
        ''' Determines a node's height 
            Args:
                nodo(Node)
        '''
        if (nodo == None):
            return 0
        else:
            alturaIzquierdo = self.alturaRecursivo(nodo.getHijoIzquierdo())
            alturaDerecho = self.alturaRecursivo(nodo.getHijoDerecho())
            
            if (alturaIzquierdo > alturaDerecho):
                return alturaIzquierdo + 1
            else:
                return alturaDerecho + 1
            
    def existeDato(self, dato):
        ''' Go through all the AVLTree to verify if a node already
            owns a data
            Args:
                dato(int)
            Return:
                true: Data already exists in the AVLTree
                false: Data doesn't exist in the AVLTree
        '''
        if (self.esVacio()):
            return False
        nodo = self.__raiz
        while (nodo != None):
            if (dato == nodo.getData()):
                return True
            else:
                if (dato < nodo.getData()):
                    nodo = nodo.getHijoIzquierdo()
                else:
                    nodo = nodo.getHijoDerecho()
        return False
        
    def esVacio(self):
        ''' Verify if an AVLTree is empty
            Return:
                true: it's empty
                flase: it's not empty 
        '''
        if self.__raiz == None:
            return True 
        else:
            return False

    def insertar(self, dato):
        ''' Method that add a node to the AVLTree in their correct
            position by following standard rules in order to maintain
            the balance in the AVLTree
            Args:
                dato(int): data is being attempted to insert
        '''
        if (self.existeDato(dato)):
            return None
        else:
            self.__raiz = self.insertarRecursivo(self.__raiz,dato)
            #self.__raiz = self.UpdateParent()
            #self.UpdateLevel(self.__Raiz)

    def insertarRecursivo(self, nodo, dato):
        ''' Recursive Method which is in charge to complete the
            insertation of a data within the AVLTree.
            Args:
                nodo(Node): the root of the AVLTree to determine where
                            the new data is going to be inserted
                dato(int): data is being attempted to insert
            Return:
                Data has been placed in the correct location in the
                AVLTree
        '''
        if (nodo == None):
            return Nodo(dato)
        else:
            if (dato < nodo.getData()):
                nodo.setHijoIzquierdo(self.insertarRecursivo(nodo.getHijoIzquierdo(), dato))
                nodo.getHijoIzquierdo().setParent(nodo)
            else:
                if (dato > nodo.getData()):
                    nodo.setHijoDerecho(self.insertarRecursivo(nodo.getHijoDerecho(), dato))
                    nodo.getHijoDerecho().setParent(nodo)

    
    def Bros(self, nodo1, nodo2):
        if (self.esVacio()== False):
            return
        if (nodo1.getParent() == None or nodo2.getParent() == None):
            return
        if (nodo1.getParent()== nodo2.getParent()):
            return True
        else:
            return False        

    
    def FindNode(self, valor):
        ''' Method go through AVLTree looking for a node whit a 
        specific value
        Args:
            valor(int): value passed which is going to be searched 
                        within the AVLTree
        Return:
            A reference to the node of value if found 
            otherwise returns 0 
        '''
        return self.FindNodeR(self.__raiz, valor)

    def FindNodeR(self,raiz,valor):
        ''' Recursive method which is in charge to complete 
            the looking-for within the whole AVLTree
            Note: 
                This method also can be used to look for within a
                subtree by passing the subtree as an arg.
            Args:
                raiz(Node): The whole tree or a specific subtree
                valor(int): The value is being looked for
            Return:
                A reference to the node of value if found 
                otherwise returns 0 
        '''
        if raiz.getData() == valor:
            return raiz 
        elif valor < raiz.getData():
            return self.FindNodeR(raiz.getHijoIzquierdo(), valor)
        elif valor > raiz.getData():
            return self.FindNodeR(raiz.getHijoDerecho(), valor)
        else:
            return 0 


    def printInorder(self, node):
        ''' Go through all the AVLTree to print them in order '''
        if(node!=None):
            self.printInorder(node.getHijoIzquierdo())
            print(node.getData())
            self.printInorder(node.getHijoDerecho())

def main():
    print("Test of the AVLTree")
    A1 = ArbolBinario()   
    '''A1.insertar(111)
    A1.insertar(345)
    A1.insertar(90)
    A1.insertar(123)
    A1.insertar(99)
    A1.insertar(370)
    A1.insertar(420)
    A1.insertar(580)
    A1.insertar(100)
    A1.insertar(80)
    A1.insertar(70)'''
    A1.insertar(200)
    A1.insertar(350)
    A1.insertar(150)
    A1.insertar(100)
    A1.insertar(90)
    print(A1.printInorder(A1.getRoot()))
    

if __name__ == "__main__":
    main()
