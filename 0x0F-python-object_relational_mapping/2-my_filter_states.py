#!/usr/bin/python3
"""
A script that takws in an arg and displays all
the states table of database, `hbtn_0e_0_usa` where
name matches the argument
"""

import MySQLdb as db
import sys


if __name__ == "__main__":
    """
    Script to take 4 args, and use the MySQLdb module connecting
    to a MySQL server running on localhost at port 3306
    """

    d_connect = db.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])

    d_cursor = d_connect.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
            states.id ASC"
    d_cursor.execute(query.format(argv[4]))

    rows = d_cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
