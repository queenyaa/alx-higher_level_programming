#!/usr/bin/python3
"""
Prints the first state object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    script takes 3 args, uses module SQLAlchemy
    importing State and Base from model_state
    """

    user = '{}'.format(argv[1])
    password = '{}'.format(argv[2])
    db = '{}'.format(argv[3])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, password, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
