""" Lists all states from the database hbtn_0e_0_usa  """
import MySQLdb
import sys


if __name__ == "__main__":
    usuario = sys.argv[1]
    contrase = sys.argv[2]
    base_datos = sys.argv[3]

    # CONEXION LOCAL
    db = MySQLdb.connect(
        host="localhost",
        port=3306
        user=usuario
        passwd=contraseña,
        db=base_datos
    )
    # CREA CRUSOR SQL, SIRVE PARA EJECUTAR SELECT, INSERT, ETC
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # FETCH: Devuelve una lista de tuplas
    for row in cur.fetchall():
        print(row)

    # siempre hay que cerrar el cursor y la conexión
    cur.close()
    db.close()
