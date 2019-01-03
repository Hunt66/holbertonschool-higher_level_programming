#!/usr/bin/python3
""" Lists all state objects from the database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


def main(argv):
    """func - main - args"""
    if len(argv) != 5:
        print("Enter 4 arguments")
        return

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                       argv[2],
                                                                       argv[3]
                                                                       ),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    count = 0
    for state in session.query(State).order_by(State.id).all():
        if state.name == argv[4]:
            count += 1
    if count > 0:
        print(count)
    else:
        print("Not found")
    session.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
