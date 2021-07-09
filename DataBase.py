import sqlite3

def createDataBase():
    miConexion = sqlite3.connect("WinnersDataBase")
    miCursor = miConexion.cursor()
    miCursor.execute("CREATE TABLE WINNERS (NOMBRE VARCHAR(50), PRIMER_LUGAR INTEGER, SEGUNDO_LUGAR INTEGER, TERCER_LUGAR INTEGER)")
    print(" SE CREO CON EXITO LA BASE DE DATOS")
    miConexion.close()

def insertResults(namePlayer, acum1, acum2, acum3):
    miConexion = sqlite3.connect("WinnersDataBase")
    miCursor = miConexion.cursor()
    query = str("INSERT INTO WINNERS VALUES('"+namePlayer+"', '"+acum1+"', '"+acum2+"', '"+acum3+"')")
    print ("QUERY A EJECUTAR: ", query)
    miCursor.execute(query)
    print(" SE INSERTARON LOS DATOS DE FORMA EXITOSA")
    miConexion.commit()
    miConexion.close()

def consulta(namePlayer):
    miConexion = sqlite3.connect("WinnersDataBase")
    miCursor = miConexion.cursor()
    query = str("SELECT * FROM WINNERS WHERE NOMBRE='"+namePlayer+"'")
    print("QUERY A EJECUTAR: ", query)
    miCursor.execute(query)
    consulta = miCursor.fetchall()
    print("Resultado de la consulta: ", consulta)
    miConexion.close()
    return consulta

