#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
            format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True)
    # Create all the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new state to the states table
    new_state = State(name="California")
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
