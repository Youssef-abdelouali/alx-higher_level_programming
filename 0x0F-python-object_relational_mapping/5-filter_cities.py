#!/usr/bin/python3
"""
Script to list all cities of a given state from the database hbtn_0e_4_usa (SQL injection free)
"""

import MySQLdb
import sys

def cities_by_state(username, password, database, state_name):
    """
    Function to list all cities of a given state from the database hbtn_0e_4_usa

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name
        state_name (str): Name of the state to list cities for

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

    # Prepare SQL query with parameters
    query = "SELECT cities.id, cities.name FROM cities \
             JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"

    # Execute the query with parameters
    cursor.execute(query, (state_name,))

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
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call function to list cities by state
    cities_by_state(username, password, database, state_name)
