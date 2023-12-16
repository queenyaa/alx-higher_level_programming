#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of the state
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    script that takes 4 args, uses module MySQLdb
    connects to a MySQL server running on localhost, port 3306

    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <state_name>".
              format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1],
    sys.argv[2], sys.argv[3], sys.argv[4]
    """

    d_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    d_cursor = d_connect.cursor()

    d_cursor.execute("SELECT cities.id, cities.name \
                     FROM cities \
                     JOIN states ON cities.state_id = states.id \
                     WHERE states.name LIKE BINARY %(state_name)s \
                     ORDER BY cities.id ASC", {'state_name': argv[4]})

    rows = d_cursor.fetchone()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
