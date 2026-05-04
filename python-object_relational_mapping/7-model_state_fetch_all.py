#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup connection to the database
    # Arguments: username, password, database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Instantiate a session
    session = Session()

    # Query all State objects and sort them by id
    # .all() executes the query and returns a list
    states = session.query(State).order_by(State.id).all()

    # Print the results in the required format
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
