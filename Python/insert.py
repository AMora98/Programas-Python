import os
import pymysql

def main():
    os.system('cls')
    print('\n')

    #Abrir la conexión a la base de datos.
    db=pymysql.connect("localhost","root","","base")

    #n objeto cursor.
    cursor=db.cursor()

    #Ejecuta el sql query usando el método execute().
    sqlcad('INSERT INTO empleados(clave, nombre, sueldo) VALUES (1,"joejoe",1234);')
    cursor.execute(sqlcad)
    db.commit()
    #procesa una única línea usando el método fecthone().
    data=cursor.fetchone()
    print("Database version: {0}".format(data))

    #Cerramos conexión.
    db.close()

    print('\n')

if __name__=='__main__':
    main()