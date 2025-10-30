#!/usr/bin/python3
""" lists all states with a name starting with N """
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name 'N%' ORDER BY states.id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
