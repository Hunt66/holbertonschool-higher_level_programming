#!/usr/bin/python3
""" Lists all state objects from the database """

import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, MetaData, Table


def main(argv):
    """func - main - args"""
    if len(argv) != 4:
        print("Enter 3 arguments")
        return

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]),
                           pool_pre_ping = True)

    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
