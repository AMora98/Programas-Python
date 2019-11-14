"""
Nombre: crud.py
Objetivo: sql
Alumno: Andrés Eduardo Mora Alonso
Fecha: 27/09/19
"""

import os
import pymysql

def main():
    os.system('cls')
    print('\n')

    #Abrir la conexión a la base de datos.
    db=pymysql.connect("localhost","root","","semaforos")

    #n objeto cursor.
    cursor=db.cursor()

    cursor.execute('insert into estrategias(id,horario,tr,ta,tv) values ("sem1","7-10",32,3,45);')

    #Cerramos conexión.
    db.close()

    print('\n')

if __name__=='__main__':
    main()