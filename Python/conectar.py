import os
import pymysql

def main():
    os.system('cls')
    print('\n')

    #Abrir la conexión a la base de datos.
    db=pymysql.connect("localhost","root","","mecatronica")

    #n objeto cursor.
    cursor=db.cursor()

    #Ejecuta el sql query usando el método execute().
    cursor.execute("SELECT VERSION()")

    #procesa una única línea usando el método fecthone().
    data=cursor.fetchone()
    print("Database version: {0}".format(data))

    #Cerramos conexión.
    db.close()

    print('\n')

if __name__=='__main__':
    main()