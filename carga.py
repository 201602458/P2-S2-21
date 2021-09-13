import xml.etree.ElementTree as ET
from xml.dom import minidom

class Carga_archivo:
    cadena=""

    def maquinaCarga(self, link):

        try:
            tree=ET.parse(link)
            self.rootM=tree.getroot()
            self.txtM = minidom.parse(link)#aqui se pone el self.link
            print(self.txtM)
            self.maquinaCom
            
        except:
            print("Error al subir el archivo")


    def simulacionCarga(self, link):

        try:
            tree=ET.parse(link)
            self.rootS=tree.getroot()
            self.txtS = minidom.parse(link)#aqui se pone el self.link
            print(self.txtS)
            

        except:
            print("Error al subir el archivo")


                    
        