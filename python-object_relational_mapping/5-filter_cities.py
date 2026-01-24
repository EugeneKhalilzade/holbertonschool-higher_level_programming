#!/usr/bin/python3
"""
Take in the name of a state as an argument and
lists all cities of that state from the database.

"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query
    query = """
        SELECT cities.name
        FROM cities JOIN states ON cities.state_id = states.id
        WHERE states.name = %s ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    cities_list = [row[0] for row in rows]

    # Join the list into a single string separated by ", "
    print(", ".join(cities_list))

    # Close the cursor and the connection
    cursor.close()
    db.close()
