class nodo:
    def __init__(self, nombre, pasos):
        self.nombre=nombre
        self.pasos=pasos
        self.siguiente=None
        self.principio=None
        self.fin=None

import re
class lista:

    def __init__(self):
        self.inicio=None

    def push(self, nombre, pasos):
       
        nuevo=nodo(nombre, pasos)
        if self.inicio==None:
            self.inicio=nuevo
            self.inicio.principio=nuevo
            nuevo.fin=nuevo
            

        else:
            aux=self.posicion()
            aux.siguiente=nuevo
            nuevo.fin=nuevo
       
        
    def posicion(self):
        ultimo=self.inicio

        while ultimo.siguiente != None:
            ultimo=ultimo.siguiente

        return ultimo

    def mostrar(self):
        aux=self.inicio
        while aux != None:
            print(aux.nombre)
            print(aux.pasos)
            aux=aux.siguiente

    def buscar(self, nombre):
        aux=self.inicio
        while aux != None:
            if (aux.nombre)== nombre:
                self.descomponer(aux.nombre, aux.pasos)
                print(aux.nombre)
                #print(aux.pasos)
            aux=aux.siguiente
        

    def descomponer(self,nombre, pasos):
        #LnCn
        #cadena=pasos.split()
        cadena=re.split('L|C| ',pasos)

        for x in cadena:
            print(x)


        



