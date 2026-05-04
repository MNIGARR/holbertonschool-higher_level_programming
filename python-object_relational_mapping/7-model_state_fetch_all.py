#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # 1. Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # 2. Create the engine to connect to the MySQL server
    # Format: mysql+mysqldb://<user>:<password>@localhost:3306/<database>
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ), pool_pre_ping=True
    )

    # 3. Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4. Query the State objects, sorted by id
    states = session.query(State).order_by(State.id).all()

    # 5. Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # 6. Close the session
    session.close()
