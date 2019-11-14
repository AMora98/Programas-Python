"""
Nombre: circunferencia.py
Objetivo: Construye objeto circunferencia.
Fecha: 20/09/19
"""

import os
import math
from eucl import punto

class circunferencia(punto):
    #Método constructor.
    def __init__(self,valorx,valoy,vradio):
        self.x=valorx
        self.y=valory
        self.radio=vradio
    
    #Método get.
    def getradio(self):
        return self.radio
    
    #Método set.
    def setradio(self,vradio):
        self.radio=vradio
    
    #Método print.
    def printradio(self):
        return 'Circunferencia con centro en: '+str(self.x)+str(self.y)+' y radio igual a: '+str(self.radio)+' de área: '+str(self.getarea())

    #Método para calcular el área.
    def getarea(self):
        return math.pi*math.pow(self.radio,2)

def main():
    os.system('cls')
    print('\n')

    print('\n')

if __name__=='__main__':
    main()