from tkinter import filedialog
from tkinter import *
from tkinter import filedialog as fd
import sys
import os
import subprocess
from datetime import datetime
from tkinter import messagebox

class proyecto:
    ventana=Tk()

    def __init__(self):
        self.crearMenu()
        
        proyecto.ventana.geometry("900x500+0+0")
       
        
        proyecto.ventana.mainloop()

    def crearMenu(self):
        barra=Menu(proyecto.ventana)
        

        menu1=Menu(barra)
        menu2=Menu(barra)
        menu3=Menu(barra)

        barra.add_cascade(label="Cargar", menu=menu1)
        barra.add_cascade(label="Reportes", menu=menu2)
        barra.add_cascade(label="Ayuda", menu=menu3)
        ##

        menu1.add_command(label="Cargar Archivo De Maquina", command=self.archivoMaquina)
        menu1.add_command(label="Cargar Archivo De Productos", command=self.archivoProducto)

        menu3.add_command(label="Informacion" , command=self.info)

       

        

      

     
        proyecto.ventana.config(menu=barra)

    def archivoMaquina(self):
        #nombreArch=proyecto.ventana.filename
        nombreArch= filedialog.askopenfilename(initialdir = r"C:\Users\Administrator\Desktop",title = "Select file",filetypes = (("xml files","*.xml"),("all files","*.*")))
        #nombreArch = fd.askopenfilename(initialdir=r"C:\Users\Administrator\Desktop\proyecto2\proyecto2.py", title="Seleccione archivo", filetypes=("xml files","*.xml"))
        if nombreArch != '':
            arch=open(nombreArch, "r", encoding="utf-8")
            contenido=arch.read()
            arch.close()
            #self.leer=lectura.leer(contenido)
        print(contenido)

        #self.mostrar()

    def archivoProducto(self):
        #nombreArch=proyecto.ventana.filename
        nombreArch= filedialog.askopenfilename(initialdir = r"C:\Users\Administrator\Desktop",title = "Select file",filetypes = (("xml files","*.xml"),("all files","*.*")))
        #nombreArch = fd.askopenfilename(initialdir=r"C:\Users\Administrator\Desktop\proyecto2\proyecto2.py", title="Seleccione archivo", filetypes=("xml files","*.xml"))
        if nombreArch != '':
            arch=open(nombreArch, "r", encoding="utf-8")
            contenido=arch.read()
            arch.close()
            #self.leer=lectura.leer(contenido)
        print(contenido)

        #self.mostrar()

    def info(self):
        texto='''
        Maria Luisa Fernanda Calderon Molina \n
        Carnet: 201602458 \n
        INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 \n
        Sección A
        '''
        messagebox.showinfo('datos', texto)


cosa = proyecto()