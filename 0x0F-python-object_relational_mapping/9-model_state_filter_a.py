#!/usr/bin/python3
"""
Script to list all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_letter_a(username, password, database):
    """
    Function to list all State objects that contain the letter 'a'
    from the database hbtn_0e_6_usa

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): Database name

    Returns:
        None
    """
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states containing letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call function to list states containing letter 'a'
    list_states_with_letter_a(username, password, database)
