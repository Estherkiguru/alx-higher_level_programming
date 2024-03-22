#!/usr/bin/python3
"""
Define the State class and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

metdata = MetaData()
Base = declarative_base(metadata=metdata)


class State(Base):
    """
    Class representing a state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")

