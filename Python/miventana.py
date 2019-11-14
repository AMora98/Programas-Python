"""
Nombre: miventana.py
Objetivo: construir interfaz gráfica.
Autor: alumnos de Mecatrónica
Fecha: 01102019
"""

from tkinter import *
from tkinter import ttk
import os

def main():
    os.system('cls')
    print("\n")

    #Creamos la ventana.
    v=Tk()
    #Modificamos las dimensiones.
    v.geometry('800x800')
    #Título en la barra.
    v.title('Captura de datos')
    #Etiquetas.
    clave=Label(v, text='Clave', font=('Arial Bold',20))
    clave.grid(column=0, row=0)

    descripcion=Label(v,text='Descripción', font=('Arial Bold',20))
    descripcion.grid(column=0, row=5)

    precio=Label(v,text='Precio', font=('Arial Bold',20))
    precio.grid(column=0, row=10)

    #Entrada de datos.
    txtClave=Entry(v,width=10)
    txtClave.grid(column=10,row=0)
    txtDescripcion=Entry(v,width=10)
    txtDescripcion.grid(column=10,row=5)
    txtPrecio=Entry(v,width=10)
    txtPrecio.grid(column=10,row=10)

    #Botones.
    guardar=Button(v,text='Guardar')
    guardar.grid(column=20,row=20)
    cancelar=Button(v,text='Cancelar')
    cancelar.grid(column=20,row=40)

    #Ciclo de espera.
    v.mainloop()

    print('\n')

if __name__=='__main__':
    main()