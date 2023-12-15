#!/usr/bin/python3
"""
Script to take an arg and display all
values of states in table of database
where name matches the argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Script should take3 args
    and use MySQLdb module
    """

    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MysQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to select and display states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    #Dispay the results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
