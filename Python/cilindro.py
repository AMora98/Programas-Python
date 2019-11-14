"""
Nombre: cilindro.py
Objetivo: Construye objeto cilindro.
Fecha: 20/09/19
"""

import os
from circunferencia import circunferencia

class cilindro(circunferencia):
    #Método constructor.
    def __init__(self,valorx,valory,vradio,altura):
        self.x=valorx
        self.y=valory
        self.radio=vradio
        self.h=altura

    #Método get.
    def getaltura(self):
        return self.h

    #Método set.
    def setaltura(self,altura):
        self.h=altura

    #Método print.
    def printcilindro(self):
        return 'Circunferencia con centro en: ['+str(self.x)+','+str(self.y)+'], y radio igual a: '+str(self.radio)+', de área: '+str(self.getarea())+', de altura: '+str(self.h)+', con volumen de: '+str(self.getvolumen())

    #Método para volumen.
    def getvolumen(self):
        return self.getarea()*self.getaltura()

def main():
    os.system('cls')
    print('\n')

    print('\n')

if __name__=='__main__':
    main()