from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
import sys
import os
import subprocess
from datetime import datetime
from tkinter import messagebox
import carga

class proyecto:
    ventana=Tk()
    var=carga.Carga_archivo()

    def __init__(self):
        self.crearMenu()
        
        proyecto.ventana.geometry("900x500+0+0")
       
        
        proyecto.ventana.mainloop()

    def crearMenu(self):
        barra=Menu(proyecto.ventana)
        #
        

        self.menu1=Menu(barra)
        menu2=Menu(barra)
        menu3=Menu(barra)

        barra.add_cascade(label="Cargar", menu=self.menu1)
        barra.add_cascade(label="Reportes", menu=menu2)
        barra.add_cascade(label="Ayuda", menu=menu3)
        ##

        self.menu1.add_command(label="Cargar Archivo De Maquina", command=self.archivoMaquina)
        self.menu1.add_command(label="Cargar Archivo De Simulacion",state = 'disabled', command=self.archivoProducto)

        menu3.add_command(label="Informacion" , command=self.info)
        #self.habilitar=menu1.entryconfig("Cargar Archivo De Simulacion", state="normal")

        tc1=Entry(proyecto.ventana)
        tc1.grid(row=5, column=2, padx=10, pady=10)
        lc1=Label(proyecto.ventana, text="Simular Producto")
        lc1.grid(row=5, column=1, padx=10, pady=10)
        btn=Button(proyecto.ventana, text="Buscar")
        btn.grid(row=5, column=3, padx=10, pady=10)

        lc2=Label(proyecto.ventana, text="Producto")
        lc2.grid(row=7, column=2, padx=10, pady=10)

        lc3=Label(proyecto.ventana, text="pasos")
        lc3.grid(row=8, column=2, padx=10, pady=10)

        self.tabla()


     
        proyecto.ventana.config(menu=barra)


    def archivoMaquina(self):
        #nombreArch=proyecto.ventana.filename
        nombreArch= filedialog.askopenfilename(initialdir = r"C:\Users\Administrator\Desktop",title = "Select file",filetypes = (("xml files","*.xml"),("all files","*.*")))
        #nombreArch = fd.askopenfilename(initialdir=r"C:\Users\Administrator\Desktop\proyecto2\proyecto2.py", title="Seleccione archivo", filetypes=("xml files","*.xml"))
        #if nombreArch != '':
        #    arch=open(nombreArch, "r", encoding="utf-8")
        #    contenido=arch.read()
        #    arch.close()
            #self.leer=lectura.leer(contenido)
        #print(nombreArch)
        self.var.maquinaCarga(nombreArch)
        self.menu1.entryconfig("Cargar Archivo De Simulacion", state="normal")
        #self.habilitar
        

        #self.mostrar()

    def archivoProducto(self):
        #nombreArch=proyecto.ventana.filename
        nombreArch= filedialog.askopenfilename(initialdir = r"C:\Users\Administrator\Desktop",title = "Select file",filetypes = (("xml files","*.xml"),("all files","*.*")))
        #nombreArch = fd.askopenfilename(initialdir=r"C:\Users\Administrator\Desktop\proyecto2\proyecto2.py", title="Seleccione archivo", filetypes=("xml files","*.xml"))
        
        self.var.simulacionCarga(nombreArch)
        #self.mostrar()

    def info(self):
        texto='''
        Maria Luisa Fernanda Calderon Molina \n
        Carnet: 201602458 \n
        INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 \n
        Sección A
        '''
        messagebox.showinfo('datos', texto)

    def tabla(self):
        tabla=ttk.Treeview(self.ventana, columns=2)
        tabla.grid(row=7,column=9,columnspan=2,padx=10, pady=10)
        tabla.heading("#0", text="linea1")
        tabla.heading("#1", text="linea2")


cosa = proyecto()