#!/usr/bin/python3
"""
Script to list all states in a
vertical format from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    Access to the database and states from
    the database
    """

    d_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    # Create a cursor object to interact with the database
    d_cursor = d_connect.cursor()

    # Execute the query to select and display states

    d_cursor.execute("SELECT id, name FROM states ORDER BY states.id ASC")

    # Fetch all the rows
    rows = d_cursor.fetchall()

    for row in rows:
        print(row)

    # d_connect.close()
