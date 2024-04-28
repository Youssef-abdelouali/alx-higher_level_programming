#!/usr/bin/python3
"""
Script to display all values in the states table of hbtn_0e_0_usa where name matches the provided argument (safe from SQL injection)
"""

import MySQLdb
import sys

def safe_search_states(username, password, database, state_name):
    """
    Function to search for states matching the provided name in the database (safe from SQL injection)

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name
        state_name (str): State name to search for

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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with parameters
    cursor.execute(query, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Print results
    for state in results:
        print(state)

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

    # Call function to search for states (safe from SQL injection)
    safe_search_states(username, password, database, state_name)
