#!/usr/bin/python3
"""
Script to change the name of a State object from the database
hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine
from sys import argv


if __name__ = "__main__":
    """
    takes 3 args, uses the SQLAlchemy
    imports State and Base from model_state
    """

    d_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(d_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
