"""
Nombre: estudiante.py
Objetivo: Clase estudiante.
Autor: Andrés Eduardo Mora Alonso.
Fecha: 24/09/19
"""

import os
from persona import persona

class estudiante(persona):

    #Constructor.
    def __init__(self,name,sur,sex,car,sch,ctrl):
        #Invocamos constructor de la superclase.
        persona.__init__(self,name,sur,sex)

        #Agregamos atributor a la clase.
        self.car=car
        self.sch=sch
        self.ctrl=ctrl

    #Métodos get. Regresa el valor de los atributos.
    def getCar(self):
        return self.car
    def getSch(self):
        return self.car
    def getCtrl(self):
        return self.ctrl

    #Métodos set.
    def setCar(self,car):
        self.car=car
    def setSch(self,sch):
        self.sch=sch
    def setCtrl(self,ctrl):
        self.ctrl=ctrl

    #Método print atributos.
    def prt(self):
        return persona.printperson(self)+'     Carrera: '+self.car+'     Escuela: '+self.sch+'     No. Control: '+str(self.ctrl)

def main():
    os.system('cls')
    print('\n')

    print('\n')

if __name__=='__main__':
    main()