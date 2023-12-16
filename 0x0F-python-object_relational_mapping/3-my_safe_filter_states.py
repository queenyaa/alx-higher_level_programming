#!/usr/bin/python3
"""
Script to delete all records of a table and
safe from MySQL injections
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    Script to take 4 arguments, use the MySQLdb module
    and connect to localhost, port 3306

    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".
              format(sys.argv[0]))
        sys.exit(1)
    """

    username, password, database, state_name = sys.argv[1],
    sys.argv[2], sys.argv[3], '{}'.format(argv[4])

    d_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = d_connect.cursor()

    cursor.execute("SELECT id, name FROM states WHERE name = %s\
                    ORDER BY states.id ASC", (state_name,))

    row = cursor.fetchall()

    for row in rows:
        print(row)
