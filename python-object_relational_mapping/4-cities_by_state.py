#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments: mysql username, mysql password and database name
Results must be sorted in ascending order by cities.id"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost"
        port=3306
        user=argv[1]
        passwd=argv[2]
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities INNER JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
