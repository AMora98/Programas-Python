"""
Nombre: mainEucl.py
Objetivo: Instanciar la clase punto.
Fecha: 20/09/19
"""

import os
from eucl import punto
from cilindro import cilindro

def main():
    os.system('cls')
    print('\n')

    a=cilindro(1,2,3,4)
    printcilindro()


if __name__=='__main__':
    main()