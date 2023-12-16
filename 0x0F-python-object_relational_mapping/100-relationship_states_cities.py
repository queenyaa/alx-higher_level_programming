#!/usr/bin/python3

"""
Script to create the State "California" with "San Francisco" from
database 'hbtn_0e_100_usa'
"""

from sys import argv
from sqlalchemy.orm.session import sessionmaker, Session
from relationship_state import Base, State
from sqlalchemy import create_engine
from relationship_city import City


if __name__ == "__main__":
    """
    takes 3 args and uses the SQLAlchemy model, connects to MySQL server
    running on localhost at port 3306, uses cities relationship for all
    State objects
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

    n_state = State(name='California')
    n_city = City(name='San Francisco', state=n_state)
    n_state.cities.append(n_city)

    session.add(n_state)
    session.add(n_city)

    session.commit()
