
class nodo:
    def __init__(self, numero, componente, tiempo):
        self.numero=numero
        self.componente=componente
        self.tiempo=tiempo
        self.anterior=None
        self.siguiente=None

class lista:
    def __init__(self):
        self.inicio=None
        self.fin=None

    def crear(self, numero, componente, tiempo):

        nuevo = nodo(numero,componente,tiempo)

        if self.inicio==None:#cola vacia
           
            self.inicio=nuevo
            
           
        else:
            
            aux=self.posicion()
            self.fin=nuevo
            self.fin.anterior=aux
            aux.siguiente=self.fin



    def posicion(self):
        ultimo=self.inicio

        while ultimo.siguiente != None:
            ultimo=ultimo.siguiente

        return ultimo

    def mostrar(self):
        aux= self.inicio
        while aux != None:
            print(aux.numero)
            print(aux.componente)
            print(aux.tiempo)


            aux=aux.siguiente



