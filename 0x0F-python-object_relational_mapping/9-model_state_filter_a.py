#!/usr/bin/python3
"""
Script to list all State objects that contain the letter
'a' from the database `hbtn_0e_6_usa`
"""

from model_state import State, Base
from sys import argv
from sqlalchemy.orm.session import sessionmaker, Session
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

    for state in session.query(State).order_by(State.id):
        if 'a' in state.name:
            # for state in states:
            print('{}: {}'.format(state.id, state.name))
