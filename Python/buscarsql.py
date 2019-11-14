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
    sqlcad='SELECT * FROM plcs;'
    cursor.execute(sqlcad)
    db.commit()
    resultado=cursor.fetchall()
    for row in resultado:
        clave=row[0]
        descripcion=row[1]
        precio=row[2]
        print('clave={0}, descripcion={1}, marca={2}'.format(clave,descripcion,precio))

    #Cerramos conexión.
    db.close()

    print('\n')

if __name__=='__main__':
    main()