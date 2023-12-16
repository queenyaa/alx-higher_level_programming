#!/usr/bin/python3
"""
Script to take an arg and display all
values of states in table of database
where name matches the argument
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    Script should take3 args
    and use MySQLdb module

    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    """

    # Extract command-line arguments
    # username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MysQL server
    d_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    d_cursor = d_connect.cursor()

    # Execute the query to select and display states starting with 'N'
    d_cursor.execute(
             """SELECT * FROM states
             WHERE name LIKE BINARY 'N%'
             ORDER BY id;"""
    )

    # Fetch all the rows
    rows = d_cursor.fetchall()

    # Dispay the results
    for row in rows:
        # if row[1][0] == 'N':
        print(row)
