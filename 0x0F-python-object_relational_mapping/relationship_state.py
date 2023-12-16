#!/usr/bin/python3
"""
Start link class to table in database
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    class to define properties of the States column
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False,
                autoincrement=True, unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade='all, delete', backref='state')
