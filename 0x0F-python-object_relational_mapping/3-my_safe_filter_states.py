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

    d_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    d_cursor = d_connect.cursor()

    d_cursor.execute("SELECT id, name FROM states WHERE name LIKE \
                    BINARY %(s_name)s ORDER BY states.id ASC",
                    {'s_name': argv[4]})

    rows = d_cursor.fetchall()

    for row in rows:
        print(row)
