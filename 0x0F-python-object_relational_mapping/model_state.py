#!/usr/bin/python3

""" Contains the class definition of State and an instance Base """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State Object deffinition """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
