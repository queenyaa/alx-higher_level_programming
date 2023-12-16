#!/usr/bin/python3
"""
Script to add State object 'Louisiana' to the database
'hbtn_0e_6_usa'
"""

from model_state import State, Base
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    """
    Script takes 3 arguments, use the SQLAlchemy module
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

    n_state = State(name="Louisiana")
    session.add(n_state)

    for state in session.query(State).filter(State.name == 'Louisiana'):
        print('{}'.format(state.id))

    session.commit()
