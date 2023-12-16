#!/usr/bin/python3
"""
Script to change the name of a State object from the database
hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    """
    takes 3 args, uses the SQLAlchemy
    imports State and Base from model_state
    """

    user = '{}'.format(argv[1])
    password = '{}'.format(argv[2])
    db = '{}'.format(argv[3])

    d_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, password, db)

    engine = create_engine(d_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})

    session.commit()
