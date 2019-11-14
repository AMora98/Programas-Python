"""
Nombre: insert.py
Objetivo: borrar registros en la tabla empleados.
Autor: alumnos de Mecatrónica
Fecha: 01102019
"""

# Importamos la libreria mysql
import pymysql
import os

clave=0
nombre=''
sueldo=0

def main():
    os.system('cls')
    print("\n")

    ############### CONFIGURAR ESTO ###################
    # Abre conexion con la base de datos crud
    db = pymysql.connect("localhost","root","","mecatronica")
    ##################################################

    ##################################################
    #Nombre de la base de datos: workersdb
    #Nombre de la tabla: tabla
    ##################################################

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # cadena sql de insercion
    n=int(input('Clave del registro a eliminar: '))
    sqlcad='"DELETE FROM plcs WHERE clave='+str(n)+'";'
    cursor.execute(sqlcad)
    #db.commit()
    print ("Operación realizada...")
    print('\n')

    # desconecta del servidor
    db.close()

    print('\n')

if __name__=='__main__':
    main()