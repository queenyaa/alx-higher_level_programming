#!/usr/bin/python3
"""
Script to list all State objects that contain the letter
'a' from the database `hbtn_0e_6_usa`
"""

from model_state import State, Base
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    """
    takes 3 args, uses the SQLAlchemy model
    imports State and Base
    """

    d_url = "mysql+mysqldb://{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(d_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name.contains('a'))
    if states is not None:
        for state in states:
            print('{0}: {1}'.format(state.id, state.name))
