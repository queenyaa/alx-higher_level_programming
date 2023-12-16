#!/usr/bin/python3
"""
Script to print the first State object from
the database, `hbtn_0e_6_usa`
"""

from model_state import State, Base
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    """
    Script that takes 4 args, use the SQLAlchemy module
    import model_state and connect to localhost at port 3306 of MySQL server
    that is running
    """

    d_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(d_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id).filter(
                State.name == func.binary(argv[4])).first()
    if state:
        print('{}'.format(state.id))
    else:
        print("Not found")
