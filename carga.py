import xml.etree.ElementTree as ET
from xml.dom import minidom
import circular
import ensamblaje
import trabajo

class Carga_archivo:
    cadena=""
    var = circular.lista()
    varT = trabajo.lista()
    varE = ensamblaje.lista()

    def maquinaCarga(self, link):

        #try:
        tree=ET.parse(link)
        self.rootM=tree.getroot()
        #self.txtM = minidom.parse(link)#aqui se pone el self.link
        #print(self.txtM)
        #print(self.rootM)
        self.maquinaCom()
            
        #except:
        #    print("Error al subir el archivo")


    def maquinaCom(self):
        #print(self.rootM[1][0].attrib)
        num=""
        cantidad=""
        tiempo=""
        nombre=""
        orden=""

        for elem in self.rootM:
            for subelem in elem:
                for sub2 in subelem:
                    #print(sub2.tag)
                    #print(sub2.text)
                    #self.var=listaDoble.lista()
                    if sub2.tag =="Numero":
                        num=sub2.text
                    if sub2.tag =="CantidadComponentes":
                        cantidad=sub2.text
                    if sub2.tag =="TiempoEnsamblaje":
                        tiempo=sub2.text
                        self.var.crear(num,cantidad,tiempo)
                        #self.varE.crearCabeza(num,cantidad,tiempo)

                    if sub2.tag =="nombre":
                        nombre=sub2.text

                    if sub2.tag =="elaboracion":
                        orden=sub2.text
                        self.varT.push(nombre,orden)

        #self.var.mostrar()
        #self.varT.mostrar()



    def simulacionCarga(self, link):

        #try:
        tree=ET.parse(link)
        self.rootS=tree.getroot()
        #self.txtS = minidom.parse(link)#aqui se pone el self.link
        #print(self.txtS)
        self.simulacionCom()

        #except:
        #    print("Error al subir el archivo")

    def simulacionCom(self):
        for elem in self.rootS:
            print(elem.tag)
            print(elem.text)
            for subelem in elem:
                self.varT.buscar(subelem.text)
                #print(subelem.tag)
                #print(subelem.text)



