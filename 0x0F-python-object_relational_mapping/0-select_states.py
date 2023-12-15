#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to select and display states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
