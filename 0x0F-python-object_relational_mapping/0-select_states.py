#!/usr/bin/python3
""" prints all states in database hbtn_0e_0_usa """
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(sys.argv[3], echo=True)
