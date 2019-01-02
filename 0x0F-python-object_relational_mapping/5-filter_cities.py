#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def main(argv):
    """func - main - args"""
    if len(argv) != 5:
        print("Enter 4 arguments")
        return

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id "
                "= states.id WHERE states.name = %s ORDER BY cities.id",
                (argv[4],))

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
