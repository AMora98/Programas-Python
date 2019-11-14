"""
Nombre: eucl.py
Objetivo: Generar objetos tipo punto.
Alumno: Andrés Eduardo Mora Alonso
Fecha: 20/09/19
"""

import os

class punto(object):
    #Método constructor.
    def __init__(self,valorx,valory):
        #Definimos atributos de la clase.
        self.x=valorx
        self.y=valory

    #Lista de métodos get.
    def getx(self):
        return self.x
    def gety(self):
        return self.y

    #Lista de métodos set.
    def setx(self,valorx):
        self.x=valorx
    def sety(self,valory):
        self.y=valory

    def printpunto(self):
        return 'Coordenadas: '+str(self.x)+', '+str(self.y)

def main():
    os.system('cls')
    print("\n")

    print('\n')

if __name__=='__main__':
    main()