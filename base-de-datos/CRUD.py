import mysql.connector
from mysql.connector import Error

def menu():
    print("\n ---- MENU CRUD ---- \n1) Ver registros \n2) Insertar registro \n3) Actualizar registro \n4) Borrar registro \n5) Salir")
    option = input("Ingrese una opcion: ")

    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='proyecto1_bd',
            user='root',
            password=''
        )
        if option == "1":
            tabla_elegida = input("Ingrese el nombre de la tabla: ")


            cursor = connection.cursor()
            cursor.execute("SELECT * FROM " + tabla_elegida)
            resultado = cursor.fetchall()

            for el in resultado:
                print(el)

            menu()
        elif option == "2":
            tabla_elegida = input("Ingrese el nombre de la tabla: ")

            cursor = connection.cursor()
            cursor.execute(f"SHOW COLUMNS FROM {tabla_elegida}")
            resultado = cursor.fetchall()

            print("--- Complete los campos ---")

            campos = "";
            insercion = "";
            for el in resultado:
                campos += el[0] + ","

                insertar = input(f'{el[0]}(tipo = {el[1]}): ')
                if insertar == "":
                    insercion += f'"{insertar}"'
                if 'varchar' in el[1] or 'date' in el[1]:
                    insercion += f'"{insertar}"' + ","
                else:
                    insercion += insertar + ","

            cursor2 = connection.cursor()
            cursor2.execute(f"INSERT INTO {tabla_elegida}({campos[0:-1]}) VALUES ({insercion[0:-1]})")
            connection.commit()
            print("¡Insercion existosa!")
            menu()
        elif option == "3":
            tabla_elegida = input("Ingrese el nombre de la tabla: ")
            id_elegido = input("Ingrese el id del registro que desea modificar: ")

            cursor = connection.cursor()
            cursor.execute(f"SHOW COLUMNS FROM {tabla_elegida}")
            resultado = cursor.fetchall()

            print("--- Actualice los campos ---")

            campos = ""

            for el in resultado:

                insertar = input(f'{el[0]}(tipo = {el[1]}): ')
                if insertar == "":
                    campos += f"{el[0]} = " + f'"{insertar}"'
                if 'varchar' in el[1] or 'date' in el[1]:
                    campos += f"{el[0]} = " + f'"{insertar}",'
                else:
                    campos += f"{el[0]} = " + f'"{insertar}",'

            cursor = connection.cursor()
            cursor.execute(f"UPDATE {tabla_elegida} SET {campos[0:-1]} WHERE {resultado[0][0]} = '{id_elegido}'")
            connection.commit()
            print("¡Actualizacion existosa!")
            menu()
        elif option == "4":
            tabla_elegida = input("Ingrese el nombre de la tabla: ")
            id_elegido = input("Ingrese el id del registro que desea eliminar: ")

            cursor = connection.cursor()
            cursor.execute(f"SHOW COLUMNS FROM {tabla_elegida}")
            resultado = cursor.fetchall()

            cursor2 = connection.cursor()
            cursor2.execute(f"DELETE FROM {tabla_elegida} WHERE {resultado[0][0]} = '{id_elegido}'")
            connection.commit()

            print("¡Eliminacion exitosa!")
            menu()
        elif option == "5":
            return

    except Error as e:
        print("Error al intentar conectarse a la base de datos.");
        menu()
    finally:
        if connection.is_connected():
            connection.close()


menu()

