#!/usr/bin/python3

"""
script
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City Class

    Attributes:
        __tablename__ (str): table name of the class
        id (int): id of the class
        name (str): name of the class
        state_id (int): state of the city
    """

    __tablename__ = 'cities'

    id = Column(Integer, nullable=False,
                autoincrement=True, unique=True,
                primary_key=True)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
