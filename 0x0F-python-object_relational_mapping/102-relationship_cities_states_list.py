#!/usr/bin/python3

"""
script that lists all City objects from the
database 'hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sys import argv
from relationship_state import Base, State
from sqlalchemy.orm.session import sessionmaker, Session
from relationship_city import City


if __name__ == '__main__':
    """
    script takes 3 args, uses the SQLAlchemy, connects to
    MySQL server on localhost at port 3306
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

    for city in session.query(City).order_by(City.id):
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
