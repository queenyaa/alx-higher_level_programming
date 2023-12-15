#!/usr/bin/python3
"""
Script to add State object 'Louisiana' to the database
'hbtn_0e_6_usa'
"""

from model_state import State and Base
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    """
    Script takes 3 arguments, use the SQLAlchemy module
    imports State and Base from model_state
    """

    d_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(d_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    n_state = State(name="Louisiana")
    session.add(n_state)
    session.commit()

    print('{0}'.format(n_state.id))
    session.close()
