#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and states from
    the database
    """
    d_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]

    # Create a cursor object to interact with the database
    cursor = d_connect.cursor()

    # Execute the query to select and display states
    cursor.execute("SELECT * FROM states")

    # Fetch all the rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)
