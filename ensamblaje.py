class nodo:
    def __init__(self, texto,cantidad,tiempo):
        self.texto=texto
        self.cantidad=cantidad
        self.tiempo=tiempo
        self.anterior=None
        self.siguiente=None
        self.arriba=None
        self.abajo=None
import carga as VC

class lista:
    def __init__(self):
        self.inicio=None

    def crearCabeza(self, linea, tiempo):
        VC.Carga_archivo.var.mostrar()



        

    def posicion(self):
        ultimo=self.inicio

        while ultimo.abajo != None:
            ultimo=ultimo.abajo

        return ultimo


    def posicion2(self,nodo):
        ultimo=nodo

        while ultimo.siguiente != None:
            ultimo=ultimo.siguiente

        return ultimo

    def mostrar(self):
        aux1=self.inicio
        aux2=self.inicio

        while aux1 != None:
            #print(str(aux1.numero)+'/'+str(aux1.componente)+'/'+str(aux1.tiempo))
            while aux2 != None:
                print(str(aux2.numero)+'/'+str(aux2.componente)+'/'+str(aux2.tiempo))
                aux2=aux2.siguiente

            aux1=aux1.abajo
            aux2=aux1
            





