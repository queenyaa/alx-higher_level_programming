#!/usr/bin/python3
"""
Script to define the City class that inherits from Base of model_state
links to the MySQL table cities
"""

from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    """
    Script to print all city objects from the database hbtn_0e_14_usa
    imports State and Base from model_state
    """

    d_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(d_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(Citry, State).join(State)

    for city, state in resilt.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
