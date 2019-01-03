#!/usr/bin/python3
""" Counts instences of a certain state """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


def main(argv):
    """func - main - args"""
    if len(argv) != 4:
        print("Enter 3 arguments")
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                       argv[2],
                                                                       argv[3]
                                                                       ),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    dele = session.query(State).filter(State.name.like('%a%')).all()
    for i in dele:
        session.delete(i)
    session.commit()

    session.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
