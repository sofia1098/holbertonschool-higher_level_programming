#!/usr/bin/python3
"""Write a script that takes the name of a state
as an argument and lists all cities of that state."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    state_name = argv[4] 

    cur = db.cursor()
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    names = [row[0] for row in rows]
    print(", ".join(names))

    cur.close()
    db.close()
