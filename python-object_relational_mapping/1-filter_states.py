#!/usr/bin/python3
"""
Filters all states from the database hbtn_0e_0_usa
and lists only the ones that start with "N".

"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("""
        SELECT id, name FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY id ASC
    """)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print results in the required format
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
