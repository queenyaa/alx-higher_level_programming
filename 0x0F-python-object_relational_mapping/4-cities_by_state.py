#!/usr/bin/python3
"""
Script to list all cities from database
'hbtn_0e_4_usa'
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    script takes 3 arfs, uses MySQLdb module
    connects to a MySQL server running on localhost port 3306

    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".
              format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    """

    d_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    d_cursor = d_connect.cursor()

    d_cursor.execute("SELECT cities.id, cities.name, states.name\
                     FROM cities JOIN states ON cities.state_id = states.id\
                     ORDER BY cities.id ASC")

    rows = d_cursor.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
