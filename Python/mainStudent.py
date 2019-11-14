"""
Nombre: mainStudent.py
Objetivo: Instanciar o construir objetos tipo estudiante.
Autor: Andrés Eduardo Mora Alonso.
Fecha: 24/09/19
"""

import os
from estudiante import estudiante

studentlist=[]

def main():
    os.system('cls')
    print('\n')

    yo=estudiante('Andrés','Mora',True,'Mecatrónica','Tec',16460162)
    studentlist.append(yo)

    print(yo.prt())

    print('\n')

if __name__=='__main__':
    main()