#!/usr/bin/python3
"""
Script to list all states with names starting with 'N' from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

def filter_states(username, password, database):
    """
    Function to filter states with names starting with 'N' from the database

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

    # Execute the query to select states with names starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

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
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call function to filter states
    filter_states(username, password, database)
