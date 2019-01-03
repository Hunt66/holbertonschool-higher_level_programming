#!/usr/bin/python3
""" Lists all state objects from the database """

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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    ans = session.query(state).first()
    if ans is None:
        print("Nothing")
    else:
        print(ans.id, end=': ')
        print(ans.name)
    session.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
