"""
Nombre: cilindro.py
Objetivo: Construye objeto cilindro.
Fecha: 20/09/19
"""

import os
from cilindro import cilindro

def main():
    os.system('cls')
    print('\n')

    a=cilindro(1,2,3,4)
    print(a.printcilindro())

    print('\n')

if __name__=='__main__':
    main()