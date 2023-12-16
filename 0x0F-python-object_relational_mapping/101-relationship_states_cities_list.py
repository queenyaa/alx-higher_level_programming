#!/usr/bin/python3

"""
Script to list all State objects, and corresponding City objects contained
in database 'hbtn+_0e_101_usa'
"""

from sys import argv
from sqlalchemy.orm.session import sessionmaker, Session
from relationship_state import Base, State
from sqlalchemy import create_engine
from relationship_city import City


if __name__ == '__main__':
    """
    takes 3 args, uses module SQLAlchemy connected through localhost
    port 3306
    """
    user = argv[1]
    password = argv[2]
    db = argv[3]

    d_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, password, db)

    engine = create_engine(d_url)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))
