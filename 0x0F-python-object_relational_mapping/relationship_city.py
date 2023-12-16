#!/usr/bin/python3

"""
Class that inherits from Base of model_state and linkes
to the MySQL table, cities
"""

from sqlalchemy import String, Column, Integer, ForeignKey
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Attributes:
        id: represents a column of an auto-generated, unique integer
            that can't be null and is a primary key
        name: a column of a sring with maximum char of 128
        state_id: column of integer, that can't be null and is a foreign key
    """

    __tablename__ = 'cities'

    id = Column(Integer, nullable=False,
                autoincrement=True, unique=True,
                primary_key=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
