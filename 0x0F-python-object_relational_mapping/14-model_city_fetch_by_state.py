#!/usr/bin/python3
""" Counts instences of a certain state """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys
from model_city import City


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
    ans = session.query(City).join(State).order_by(City.id).all()
    for i in ans:
        st = session.query(State).filter(State.id == i.state_id).one()
        print(st.name, end=': (')
        print(i.id, end=') ')
        print(i.name)

    session.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
