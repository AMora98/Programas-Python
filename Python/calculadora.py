"""
Nombre: miventana.py
Objetivo: interfaz gráfica de una calculadora.
Autor: alumnos de Mecatrónica
Fecha: 08/10/19
"""

from tkinter import *
from tkinter import ttk
import os

def main():
    os.system('cls')
    print("\n")

    #Crear ventana.
    v=Tk()

    #Dimensiones y fondo.
    v.geometry('450x400')
    v.configure(background='SkyBlue4')

    #Frame.
    mf=Frame(v,width=380,height=100)
    mf.place(x=30,y=20)
    mf.config(bg="#E0D8DE")

    # Pantalla de la calculadora.
    v.title('Calculadora')
    screen=Entry(mf,font=('arial',20,'bold'))
    screen.config(bg="SkyBlue")
    screen.config(width=21,bd=19,justify='right')
    screen.place(x=15,y=15)

    #Botones.
    b7=Button(v,text='7',width=5,height=2).place(x=50,y=150)
    b8=Button(v,text='8',width=5,height=2).place(x=150,y=150)
    b9=Button(v,text='9',width=5,height=2).place(x=250,y=150)
    b4=Button(v,text='4',width=5,height=2).place(x=50,y=200)
    b5=Button(v,text='5',width=5,height=2).place(x=150,y=200)
    b6=Button(v,text='6',width=5,height=2).place(x=250,y=200)
    b1=Button(v,text='1',width=5,height=2).place(x=50,y=250)
    b2=Button(v,text='2',width=5,height=2).place(x=150,y=250)
    b3=Button(v,text='3',width=5,height=2).place(x=250,y=250)
    b0=Button(v,text='0',width=5,height=2).place(x=150,y=300)
    bequal=Button(v,text='=',width=5,height=2).place(x=250,y=300)
    bdot=Button(v,text='.',width=5,height=2).place(x=50,y=300)
    bdiv=Button(v,text='/',width=5,height=2).place(x=350,y=150)
    bprod=Button(v,text='X',width=5,height=2).place(x=350,y=200)
    bmin=Button(v,text='-',width=5,height=2).place(x=350,y=250)
    bplus=Button(v,text='+',width=5,height=2).place(x=350,y=300)
    
    #Ciclo de espera.
    v.mainloop()

    print('\n')

if __name__=='__main__':
    main()