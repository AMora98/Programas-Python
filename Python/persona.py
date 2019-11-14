"""
Nombre: persona.py
Objetivo: Superclase en la jerarquía de herencia.
Autor: Andrés Eduardo Mora Alonso.
Fecha: 24/09/19
"""

import os

class persona(object):

    #Constructor.
    def __init__(self,name,sur,sex):
        self.name=name
        self.sur=sur
        self.sex=sex

    #Métodos get. Regresa el valor de los atributos.
    def getName(self):
        return self.name
    def getSur(self):
        return self.sur
    def getSex(self):
        return self.sex
    
    #Métodos set.
    def setName(self,name):
        self.name=name
    def setSur(self,sur):
        self.sur=sur
    def setSex(self,sex):
        self.sex=sex

    #Método print atributos.
    def printperson(self):
        return 'Nombre: '+self.name+' '+self.sur+'     Sexo: '+str(self.sex)

def main():
    os.system('cls')
    print('\n')

    print('\n')

if __name__=='__main__':
    main()