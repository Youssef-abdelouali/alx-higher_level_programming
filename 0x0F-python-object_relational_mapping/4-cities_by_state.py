#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

def cities_by_state(username, password, database):
    """
    Function to list all cities from the database hbtn_0e_4_usa

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name

    Returns:
        None
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select cities with their corresponding states
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    # Fetch all results
    results = cursor.fetchall()

    # Print results
    for city in results:
        print(city)

    # Close cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call function to list cities by state
    cities_by_state(username, password, database)
